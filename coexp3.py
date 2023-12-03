### Boas Pucker ###
### b.pucker@tu-braunschweig.de ###
### v0.2 ###

__usage__ = """
					python coexp3.py
					--in <FULL_PATH_TO_CANDIDATE_FILE(one ID per line)>
					--exp <FULL_PATH_TO_EXPRESSION_TABLE>
					--out <FULL_PATH_TO_OUTPUT_DIRECTORY>
					
					optional:
					--ann <FULL_PATH_TO_ANNOTATION_FILE>
					--rcut <MIN_CORRELATION_CUTOFF>
					--pcut <MAX_P_VALUE_CUTOFF>
					--expcut <MIN_EXPRESSION_CUTOFF>
					--verbose <ACTIVATES_DETAILED_OUTPUT>
					
					bug reports and feature requests: bpucker@cebitec.uni-bielefeld.de
					"""

from operator import itemgetter
import numpy as np
import re, math, sys, os
from scipy import stats

# ---- end of imports --- #

def load_expression_values( filename ):
	"""! @brief load all expression values """
	
	expression_data = {}
	with open( filename, "r" ) as f:
		tissues = f.readline().strip().split('\t')[1:]
		line = f.readline()
		while line:
			parts = line.strip().split('\t')
			expression = {}
			for idx, each in enumerate( parts[1:] ):
				expression.update( { tissues[  idx ] : float( parts[ idx+1 ] ) } )
			line = f.readline()
			expression_data.update( { parts[0]: expression } )
	return expression_data


def compare_candidates_against_all( candidate, gene_expression, rcut, pcut, expcut, verbose ):
	"""! @brief compare candidate gene expression against all genes to find co-expressed genes """
	
	if verbose:
		sys.stdout.write( candidate + "\n" )
		sys.stdout.flush()
	
	tissues = list( sorted( list( gene_expression[ list( gene_expression.keys() )[0] ].keys() ) ) )
	coexpressed_genes = []
	errors = []
	for i, gene2 in enumerate( gene_expression.keys() ):
		if candidate != gene2:
			values = []
			total_expression = 0
			for tissue in tissues:
				try:
					x = gene_expression[ candidate ][ tissue ]
					y = gene_expression[ gene2 ][ tissue ]
					total_expression += y
					if not math.isnan( x ) and not math.isnan( y ) :
						values.append( [ x, y ] )
				except KeyError:
					pass
			
			if verbose:
				sys.stdout.write( str( values ) + "\n" )
				sys.stdout.flush()
			
			try:
				r, p = stats.spearmanr( values )
				if verbose:
					sys.stdout.write( candidate + " vs. " + gene2 + "; r: " + str( r ) + "; p:" + str( p ) + "\n" )
					sys.stdout.flush()
				if not math.isnan( r ) and total_expression > expcut:
					if r > rcut and p < pcut:
						coexpressed_genes.append( { 'id': gene2, 'correlation': r, 'p_value': p } )
			except ValueError:
				errors.append( candidate )
	
	if len( errors ) > 0:
		sys.stdout.write ( "ERRORS: " + ";".join( list( set( errors ) ) ) )
		sys.stdout.flush()
	return coexpressed_genes


def load_annotation( annotation_file ):
	"""! @brief load annotation mapping table """
	
	annotation_mapping_table = {}
	
	with open( annotation_file, "r" ) as f:
		line = f.readline()
		while line:
			parts = line.strip().split('\t')
			if len( parts ) == 2:
				annotation_mapping_table.update( { parts[0]: parts[1] } )
			else:
				annotation_mapping_table.update( { parts[0]: "; ".join( parts[1:] ) } )
			line = f.readline()
	return annotation_mapping_table


def main( arguments ):
	"""! @brief run everything """
	
	expression_file = arguments[ arguments.index( '--exp' )+1 ]
	output_prefix = arguments[ arguments.index( '--out' )+1 ]
	candidate_gene_file = arguments[ arguments.index( '--in' )+1 ]
	
	if output_prefix[-1] != "/":
		output_prefix += "/"
	
	if not os.path.exists( output_prefix ):
		os.makedirs( output_prefix )
	
	if '--ann' in arguments:
		annotation_file = arguments[ arguments.index( '--ann' )+1 ]
		annotation_mapping_table = load_annotation(  annotation_file)
	else:
		annotation_mapping_table = {}
	
	if '--rcut' in arguments:
		rcut = arguments[ arguments.index( '--rcut' )+1 ]
		try:
			rcut = float( rcut )
		except:
			rcut = 0.65
	else:
		rcut = 0.65
	
	if '--pcut' in arguments:
		pcut = arguments[ arguments.index( '--pcut' )+1 ]
		try:
			pcut = float( pcut )
		except:
			pcut = 0.05
	else:
		pcut = 0.05
	
	if '--expcut' in arguments:
		expcut = arguments[ arguments.index( '--expcut' )+1 ]
		try:
			expcut = float( expcut )
		except:
			expcut = 5
	else:
		expcut = 5
	
	if "--verbose" in arguments:
		verbose = True
	else:
		verbose = False
	
	#correlation method?
	
	gene_expression = load_expression_values( expression_file )
	
	high_impact_candidates = [ ]
	
	with open( candidate_gene_file, "r" ) as f:
		line = f.readline()
		while line:
			candidate = line.strip()
			if "\t" in candidate:
				candidate = candidate.split('\t')[0]
			high_impact_candidates.append( candidate )
			line = f.readline()
	
	if verbose:
		sys.stdout.write ( "CANDIDATES:" + "\n".join( list( high_impact_candidates ) ) + "\n" )
		sys.stdout.flush()
	
	number_of_genes = float( len( list( gene_expression.keys() ) ) )
	for candidate in high_impact_candidates:
		coexpression_output_file = output_prefix + candidate + ".txt"
		if not os.path.isfile( coexpression_output_file ):
			coexpressed_genes = sorted( compare_candidates_against_all( candidate, gene_expression, rcut, pcut, expcut, verbose ), key=itemgetter( 'correlation' ) )[::-1]
			with open( coexpression_output_file, "w" ) as out:
				out.write( 'CandidateGene\tGeneID\tSpearmanCorrelation\tadjusted_p-value\tFunctionalAnnotation\n' )
				for entry in coexpressed_genes:
					try:
						out.write( "\t".join( map( str, [ candidate, entry['id'], entry['correlation'], entry['p_value'] * number_of_genes, annotation_mapping_table[ entry['id'] ] ] ) ) + '\n' )
					except KeyError:
						out.write( "\t".join( map( str, [ candidate, entry['id'], entry['correlation'], entry['p_value'] * number_of_genes, "N/A" ] ) ) + '\n' )


if '--exp' in sys.argv and '--out' in sys.argv and '--in' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )

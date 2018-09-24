// this cypher will populate all partner nodes and attributes

LOAD CSV WITH HEADERS FROM 'file:///E:/match_algo/data/raw/test/test_partner_ranks.csv' AS row

MERGE (prt:Partner {
	name: row.partner_name    
})
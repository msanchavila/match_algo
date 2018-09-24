// this cypher will populate all student rankings to partners

LOAD CSV WITH HEADERS FROM 'file:///E:/match_algo/data/raw/test/test_student_data.csv' AS row

MERGE (stu:Student {
	slate_id: row.slate_id
})

MERGE (prt:Partner {
	name: row.partner_name    
})

MERGE (stu)-[stu_rnk: StudentRank {
	rank: row.rank,
	
}]-(prt)
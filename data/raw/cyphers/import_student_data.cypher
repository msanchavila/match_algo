// this cypher will populate all student nodes and attributes

LOAD CSV WITH HEADERS FROM 'file:///E:/match_algo/data/raw/test/test_student_data.csv' AS row

MERGE (stu:Student {
	slate_id: row.slate_id
})
ON MATCH SET
	stu.first_name = row.first_name,
    stu.last_name = row.last_name,
    stu.gender = row.gender,
    stu.fin_score = row.fin_score,
    stu.ach_score = row.ach_score
ON CREATE SET
	stu.first_name = row.first_name,
    stu.last_name = row.last_name,
    stu.gender = row.gender,
    stu.fin_score = row.fin_score,
    stu.ach_score = row.ach_score
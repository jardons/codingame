SELECT TOP 10 agent.name, count(mutantid) AS SCORE
    FROM agent
        INNER JOIN mutant
            ON agentid = recruiterid
    GROUP BY agentid, agent.NAME
    ORDER BY COUNT(mutantid) DESC

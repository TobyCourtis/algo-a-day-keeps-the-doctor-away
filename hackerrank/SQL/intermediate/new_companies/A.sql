/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/


/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

-- plan
-- OUT: company_code, founder, count(lead managers), count(senior managers), count(mangers), count(employeers) order by company_code

-- COMPANY
-- company_code, founder

-- LEAD_MANAGER
-- lead_manager_code, company_code

-- SENIOR_MANAGER
-- senior_manager_code, lead_manager_code, company_code

-- MANAGER
-- manager_code, senior_manager_code, lead_manager_code, company_code

-- EMPLOYEE
-- employee_code, manager_code, senior_manager_code, lead_manager_code, company_code

-- output:
-- C1 Monika 1 2 1 2
-- C2 Samantha 1 1 2 2

SELECT
    distinct(company.company_code),
            company.founder,
            (SELECT COUNT(DISTINCT lead_manager_code) AS distinct_count FROM Lead_Manager WHERE company_code = company.company_code) as lead_manager_count,
            (SELECT COUNT(DISTINCT senior_manager_code) AS distinct_count FROM SENIOR_MANAGER WHERE company_code = company.company_code) as snr_manager_count,
            (SELECT COUNT(DISTINCT manager_code) AS distinct_count FROM MANAGER WHERE company_code = company.company_code) as manager_count,
            (SELECT COUNT(DISTINCT employee_code) AS distinct_count FROM EMPLOYEE WHERE company_code = company.company_code) as emplpyee_count
FROM COMPANY company
         JOIN Lead_Manager LM ON company.company_code = LM.company_code
         JOIN SENIOR_MANAGER SM ON LM.lead_manager_code = SM.lead_manager_code
         JOIN MANAGER M ON SM.senior_manager_code = M.senior_manager_code
         JOIN EMPLOYEE E ON M.manager_code = E.manager_code
order by company.company_code;


-- second approach:
SELECT
    company.company_code,
    company.founder,
    COUNT(DISTINCT lm.lead_manager_code) AS lead_manager_count,
    COUNT(DISTINCT sm.senior_manager_code) AS snr_manager_count,
    COUNT(DISTINCT m.manager_code) AS manager_count,
    COUNT(DISTINCT e.employee_code) AS employee_count
FROM COMPANY company
         JOIN Lead_Manager LM ON company.company_code = LM.company_code
         JOIN SENIOR_MANAGER SM ON LM.lead_manager_code = SM.lead_manager_code
         JOIN MANAGER M ON SM.senior_manager_code = M.senior_manager_code
         JOIN EMPLOYEE E ON M.manager_code = E.manager_code
group by company.company_code, company.founder -- without group by there is an issue due to many duplicates of company.company_code and company.founder
order by company.company_code;

-- corrected
-- LEFT join protects against values in the other DBs to company such as lead_manager that have rows not referring
-- to any row in company.
SELECT
    company.company_code,
    company.founder,
    COUNT(DISTINCT lm.lead_manager_code) AS lead_manager_count,
    COUNT(DISTINCT sm.senior_manager_code) AS snr_manager_count,
    COUNT(DISTINCT m.manager_code) AS manager_count,
    COUNT(DISTINCT e.employee_code) AS employee_count
FROM COMPANY company
         LEFT JOIN Lead_Manager LM ON company.company_code = LM.company_code
         LEFT JOIN SENIOR_MANAGER SM ON LM.lead_manager_code = SM.lead_manager_code
         LEFT JOIN MANAGER M ON SM.senior_manager_code = M.senior_manager_code
         LEFT JOIN EMPLOYEE E ON M.manager_code = E.manager_code
group by company.company_code, company.founder
order by company.company_code;
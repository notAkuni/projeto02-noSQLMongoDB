
# Projeto 02 - Tópicos Avançados de Banco de Dados




## Integrantes

- Gabriel Brito Schanz - RA: 22.119.010-1


## Consultas em SQL (Atividade 1)

### Consulta 01

Escreva uma query que retorna qual estudante fez qual disciplina do próprio orientador. Retorne apenas o nome do estudante, do professor e da disciplina.

```http
    SELECT student.name, student.dept_name, instructor.name AS instructor_name
    FROM student
    INNER JOIN advisor
    ON student.id = advisor.s_id
    INNER JOIN instructor
    ON instructor.id = advisor.i_id
    ORDER BY student.name
```
### Consulta 02

Qual sala (prédio e número) cada professor dá aula?

```http
    SELECT DISTINCT instructor.name, section.building, section.room_number
    FROM instructor
    INNER JOIN teaches
    ON instructor.id = teaches.id
    INNER JOIN section
    ON section.course_id = teaches.course_id
    ORDER BY section.building
```

### Consulta 03

Qual o nome, orçamento, total de alunos e salário médio de cada departamento?

```http
    SELECT d.dept_name, d.budget,
   (SELECT COUNT(s.id)
    FROM student s
    WHERE s.dept_name = d.dept_name) AS Qtde_student,
        (SELECT AVG(i.salary)
        FROM instructor i
        WHERE i.dept_name = d.dept_name) AS Avg_salary
    FROM department d
    GROUP BY d.dept_name
```

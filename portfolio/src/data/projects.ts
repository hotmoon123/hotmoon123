import type { Project } from './types';

// Content is hardcoded on purpose. Replace bracketed text with your real details.
// Only mark a status you can defend: Planned, In progress, Implemented, Tested, or Deployed.
export const projects: Project[] = [
  {
    slug: 'examination-system',
    title: 'Examination System',
    summary: '[One sentence: what the system does for lecturers and students.]',
    year: '[Year]',
    role: '[Your role: for example, sole developer or backend lead]',
    status: 'In progress',
    languages: ['PHP', 'MySQL'],
    tools: ['Git', '[Other tools]'],
    featured: true,
    hasCaseStudy: true,
    problem: '[Who needed this system, what was failing without it, and why it matters.]',
    objectives: ['[Measurable goal one]', '[Measurable goal two]'],
    features: ['[User-visible capability one]', '[User-visible capability two]'],
    architecture: ['Browser front end (HTML, CSS, JavaScript)', 'PHP application layer', 'MySQL database'],
    database: ['[Main tables and their keys]', '[One important relationship or constraint]'],
    testing: ['[What you tested and how]', '[A known defect, if any]'],
    decisions: ['[Decision, the alternative you considered, and why you chose this]'],
    results: ['[Outcome you observed or measured. Do not claim figures you did not measure.]'],
    limitations: ['[What is not finished or not yet supported]'],
    futureWork: ['[Specific next improvement]'],
    codeSample: {
      title: 'Validated, parameterised query (PHP + PDO)',
      language: 'php',
      code: `$stmt = $pdo->prepare(
    'SELECT id, title, starts_at FROM exams WHERE course_id = :course'
);
$stmt->execute([':course' => $courseId]);
$exams = $stmt->fetchAll(PDO::FETCH_ASSOC);`,
    },
  },
  {
    slug: 'python-automation',
    title: 'Python Automation Tool',
    summary: '[One sentence: the repetitive task it automates and who benefits.]',
    year: '[Year]',
    role: '[Your role]',
    status: 'Implemented',
    languages: ['Python'],
    tools: ['[Libraries used]'],
    featured: true,
    hasCaseStudy: false,
    problem: '[The manual process that was slow or error-prone.]',
    objectives: ['[Goal one]'],
    features: ['[Capability one]', '[Capability two]'],
    architecture: ['Command-line entry point', 'Processing module', 'Output or report file'],
    database: [],
    testing: ['[Test approach, for example unit tests with pytest]'],
    decisions: ['[Why you chose this structure or library]'],
    results: ['[Observed outcome]'],
    limitations: ['[Known limit]'],
    futureWork: ['[Next improvement]'],
    codeSample: {
      title: 'Small, testable function',
      language: 'python',
      code: `def normalise_rows(rows: list[dict]) -> list[dict]:
    """Strip whitespace and drop rows without an id."""
    cleaned = []
    for row in rows:
        if not row.get("id"):
            continue
        cleaned.append({k: str(v).strip() for k, v in row.items()})
    return cleaned`,
    },
  },
  {
    slug: 'cpp-algorithms',
    title: 'C++ Data Structures and Algorithms',
    summary: '[One sentence: which structures and algorithms you implemented and why.]',
    year: '[Year]',
    role: '[Your role]',
    status: 'Tested',
    languages: ['C++'],
    tools: ['g++ or clang++', 'Makefile'],
    featured: true,
    hasCaseStudy: false,
    problem: '[Why these implementations were worth building: learning goal or coursework.]',
    objectives: ['[Goal one]'],
    features: ['[Structure or algorithm one]', '[Structure or algorithm two]'],
    architecture: ['Header and source files per structure', 'Test driver'],
    database: [],
    testing: ['[Test cases, including edge cases]'],
    decisions: ['[Decision about memory management or complexity]'],
    results: ['[Observed behaviour, such as measured run times for a stated input size]'],
    limitations: ['[Known limit]'],
    futureWork: ['[Next improvement]'],
    codeSample: {
      title: 'Stack with clear ownership',
      language: 'cpp',
      code: `template <typename T>
class Stack {
public:
    void push(T value) { items_.push_back(std::move(value)); }
    T pop() {
        if (items_.empty()) throw std::underflow_error("pop on empty stack");
        T top = std::move(items_.back());
        items_.pop_back();
        return top;
    }
private:
    std::vector<T> items_;
};`,
    },
  },
];

export const getProject = (slug: string): Project | undefined =>
  projects.find((project) => project.slug === slug);

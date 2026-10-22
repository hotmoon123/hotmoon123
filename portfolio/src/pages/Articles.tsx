import PageHeader from '../components/PageHeader';
import Section from '../components/Section';
import { publishedArticles } from '../data/articles';

export default function Articles() {
  const list = publishedArticles();

  return (
    <>
      <PageHeader
        eyebrow="Articles"
        title="Technical notes"
        lead="Explanations I can defend. Articles appear here once they are published in the data file."
      />

      <Section id="list" title="Latest articles">
        {list.length > 0 ? (
          <ul className="stack-list">
            {list.map((article) => (
              <li key={article.slug} className="card" data-reveal>
                <p className="small muted">
                  {article.date} · {article.topic} · {article.readMinutes} min read
                </p>
                <h3>{article.title}</h3>
                <p className="muted">{article.summary}</p>
              </li>
            ))}
          </ul>
        ) : (
          <div className="empty-state" role="status">
            <p>No articles are published yet.</p>
          </div>
        )}
      </Section>
    </>
  );
}

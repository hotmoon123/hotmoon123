import { Fragment, useEffect, useRef } from 'react';
import { wordsIn } from '../animations/motion';

/** Splits text into words and animates them in with Anime.js. The text stays readable without JavaScript. */
export default function AnimatedWords({ text, className }: { text: string; className?: string }) {
  const ref = useRef<HTMLSpanElement>(null);
  const words = text.split(' ');

  useEffect(() => {
    if (!ref.current) return;
    wordsIn(ref.current.querySelectorAll('.word-inner'));
  }, [text]);

  return (
    <span ref={ref} className={className} aria-label={text}>
      {words.map((word, index) => (
        <Fragment key={`${word}-${index}`}>
          {index > 0 && ' '}
          <span className="word" aria-hidden="true">
            <span className="word-inner">{word}</span>
          </span>
        </Fragment>
      ))}
    </span>
  );
}

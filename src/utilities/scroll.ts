export function scrollToNext() {
  const main = document.querySelector('main, .scroll-container, #app');
  main?.scrollTo({
    top: window.innerHeight,
    behavior: 'smooth',
  });
}
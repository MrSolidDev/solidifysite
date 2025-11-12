export function scrollToNext() {
  if (typeof window === 'undefined') return;

  const main = document.querySelector('main, .scroll-container, #app');
  if (!main) {
    console.warn('No se encontró el contenedor para hacer scroll');
    return;
  }

  main.scrollTo({
    top: window.innerHeight,
    behavior: 'smooth',
  });
}
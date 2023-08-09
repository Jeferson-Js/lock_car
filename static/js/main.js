const btn = document.querySelector('button');

const toggleMenu = (e) => {
   let lista = document.querySelector('ul')
   lista.classList.toggle('hidden');
   e.name == 'menu' ? e.name = 'close' : e.name = 'menu';
}
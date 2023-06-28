const menu = document.querySelector('.hamburguesa');
const navegacion = document.querySelector('.navegacion');
const imagenes = document.querySelectorAll('img');
const btnBigotes = document.querySelector('.bigotes');
const btnChocolate = document.querySelector('.chocolate');
const btnLuna = document.querySelector('.luna');
const contenedorTestimonios = document.querySelector('.testimonios');
document.addEventListener('DOMContentLoaded',()=>{
    eventos();
    testimonios();
});

const eventos = () =>{
menu.addEventListener('click',abrirMenu);
}

const abrirMenu = () =>{
    navegacion.classList.remove('ocultar');
    botonCerrar();
}

const botonCerrar = () =>{
    const btnCerrar = document.createElement('p');
    btnCerrar.textContent ='X';
    btnCerrar.classList.add('btn-cerrar');
    
    while(navegacion.children[5]){
        navegacion.removeChild(navegacion.children[5]);
    }
    navegacion.appendChild(btnCerrar);
    cerrarMenu(btnCerrar);
}

const observer = new IntersectionObserver((entries, observer)=>{
    entries.forEach(entry=>{
        if(entry.isIntersecting){
            const imagenes = entry.target;
            observer.unobserve(imagenes);
        }
    });
});

imagenes.forEach(imagenes=>{
    imagenes.src = imagenes.dataset.src;
    observer.observe(imagenes);
});

const cerrarMenu = (boton) =>{
    boton.addEventListener('click',()=>{
       navegacion.classList.add('ocultar');

    });
}

const testimonios = () =>{
    let testimoniosArreglo = [];
    const testimonios = document.querySelectorAll('.testimonio');

    testimonios.forEach(testimonio=> testimoniosArreglo = [...testimoniosArreglo,testimonio]);

    const bigotes = testimoniosArreglo.filter(Bigotes=> Bigotes.getAttribute('data-testimonio') === 'Bigotes');
    const chocolate = testimoniosArreglo.filter(Chocolate=> Chocolate.getAttribute('data-testimonio') === 'Chocolate');
    const luna = testimoniosArreglo.filter(Luna => Luna.getAttribute('data-testimonio') === 'Luna');

    // mostrarTestimonios(bigotes, chocolate, luna);
}

/* const mostrarTestimonios = (bigotes, chocolate, luna) =>{
  btnBigotes.addEventListener('click', ()=>{
    limpiarHtml(contenedorTestimonios);
    bigotes.forEach(bigotes => contenedorTestimonios.appendChild(bigotes));
  })
} */

const limpiarHtml = (contenedor) =>{
    while(contenedor.firstChild){
        contenedor.removeChild(contenedor.firstChild);
    }
}
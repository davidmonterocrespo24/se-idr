'use strict';

//function mostrarPremio() {
//    var bloques_ocultos = document.getElementsByClassName('bloqueocultotutor');
//    var bloques = document.getElementsByClassName('bloque');
//    var numero_bloques = bloques.length - 1;
//    console.log(bloques_ocultos.length);
//
//    bloques_ocultos[0].classList.remove('bloqueocultotutor');
//
////	document.getElementById('dependiente1').style.display = 'block';
////	document.getElementById('triste').style.display = 'none';
//}

function mostrarPremio() {
	document.getElementById('bloqueocultotutor').style.display = 'block';
	document.getElementById('ver-mas').style.display = 'none';
	document.getElementById('ver-menos').style.display = 'block';
}

function ocultarPremio() {
	document.getElementById('bloqueocultotutor').style.display = 'none';
	document.getElementById('ver-mas').style.display = 'block';
	document.getElementById('ver-menos').style.display = 'none';
}
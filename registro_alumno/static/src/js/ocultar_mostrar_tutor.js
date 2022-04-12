'use strict';

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
//----------------SLIDER PANTALLA PRINCIPAL--------------------//

$('.slider').slider({full_width: true});

//----------------DROPDOWN MENU PANTALLA PRINCIPAL--------------------//

$('.dropdown-button').dropdown();

//----------------BOTON COLLAPSE PANTALLA PRINCIPAL--------------------//

$('.button-collapse').sideNav();

//----------------MODAL PANTALLA PRINCIPAL--------------------//

$('.modal-trigger').leanModal();


function cerrarModal(id){
	$('#'+id).closeModal();

}

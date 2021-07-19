/*Funcion de cargar*/
$(document).ready(function(){
    $(".button-collapse").sideNav(); //Menu del Header

    $('ul.tabs').tabs(); //Menu

    $('.parallax').parallax(); //Efecto Parallax

    $('.scrollspy').scrollSpy(); //Transicion a los elementos de forma fluida

    $('.modal-trigger').leanModal({ //Ventanas Modales (Las que aparecen derrepente :v)
          dismissible: true, // Afecto
          opacity: .7, // Opacidad de fondo
          in_duration: 300, // Duracion de la transicion al abrir
          out_duration: 250, // Duracion de la transicion al cerrar
        }
    );    

    Materialize.updateTextFields(); //Habilitar TextFields

    $('select').material_select(); //Habilitar los Select

    $('input#input_text, textarea#textarea1').characterCounter(); //Habilitar que Pueda Contar los Caracteres

    $('.datepicker').pickadate({ //Calendario
                selectMonths: true, // Habilitar la Seleccion de Meses
                selectYears: 15, // Numero de Años Posibles
                firstDay: true //Que el calendario empieze en lunes
            });

    $('.tooltipped').tooltip({delay: 50});//Mensajito en hover del boton

    $('.materialboxed').materialbox();//Efecto zoom de imagenes

    $('.NavLateral-DropDown').on('click', function(e){
        e.preventDefault();
        var DropMenu=$(this).next('ul');
        var CaretDown=$(this).children('i.NavLateral-CaretDown');
        DropMenu.slideToggle('fast');
        if(CaretDown.hasClass('NavLateral-CaretDownRotate')){
            CaretDown.removeClass('NavLateral-CaretDownRotate');    
        }else{
            CaretDown.addClass('NavLateral-CaretDownRotate');    
        }
         
    });
    
    $('.ShowHideMenu').on('click', function(){
        var MobileMenu=$('.NavLateral');
        if(MobileMenu.css('opacity')==="0"){
            MobileMenu.addClass('Show-menu');   
        }else{
            MobileMenu.removeClass('Show-menu'); 
        }   
    }); 

    $('.btn-ExitSystem').on('click', function(e){
        e.preventDefault();
        swal({ 
            title: "¿Está seguro que deseas deslogearte?",   
            text: "Está a punto de salir del sistema",   
            type: "warning",   
            showCancelButton: true,   
            confirmButtonColor: "#DD6B55",   
            confirmButtonText: "Si, Estoy Seguro",
            animation: "slide-from-top",   
            closeOnConfirm: false,
            cancelButtonText: "Cancelar"
        }, function(){
            setTimeout(function(){ window.location='/'; }, 200);
        });
    });

    $('.btn-EliminarAdmin').on('click', function(e){
        e.preventDefault();
        swal({ 
            title: "¿Estas Seguro que Deseas Deslogearte?",   
            text: "Estas Apunto de Salir del Sistema",   
            type: "warning",   
            showCancelButton: true,   
            confirmButtonColor: "#DD6B55",   
            confirmButtonText: "Si, Estoy Seguro",
            animation: "slide-from-top",   
            closeOnConfirm: false,
            cancelButtonText: "Cancelar"
        }, function(){   
            window.location='login.html'; 
        });
    }); 

    $('.btn-Search').on('click', function(e){
        e.preventDefault();
        swal({   
            title: "¿Qué Deseas Buscar?",   
            text: "Escribe lo que deseas Buscar",   
            type: "input",   
            showCancelButton: true,   
            closeOnConfirm: false,   
            animation: "slide-from-top",   
            inputPlaceholder: "Escribe Aqui",
            confirmButtonText: "Buscar",
            cancelButtonText: "Cancelar" 
        }, function(inputValue){   
            if (inputValue === false) return false;      
            if (inputValue === "") {     swal.showInputError("Debes de Escribir algo");     
            return false   
            }      
            swal("¡Bien!", "Buscaremos Informacion relacionada con: " + inputValue, "success"); 
        });    
    });

    $('.btn-Notification').on('click', function(){
        var NotificationArea=$('.NotificationArea');
        if(NotificationArea.hasClass('NotificationArea-show')){
            NotificationArea.removeClass('NotificationArea-show');
        }else{
            NotificationArea.addClass('NotificationArea-show');
        }
    });

});

/*Funcion de scroll*/
(function($){
    $(window).load(function(){
        $(".NavLateral-content").mCustomScrollbar({
            theme:"light-thin",
            scrollbarPosition: "inside",
            autoHideScrollbar: true,
            scrollButtons:{ enable: true }
        });
        $(".ContentPage, .NotificationArea").mCustomScrollbar({
            theme:"dark-thin",
            scrollbarPosition: "inside",
            autoHideScrollbar: true,
            scrollButtons:{ enable: true }
        });
    });
})(jQuery);

/* ------------ Funciones para la seccion de test ------------ */

function colorea(idImg){
    let imgs = document.querySelectorAll(".Preguntas");
    const tamPreguntas = imgs.length;
    let imagen = document.getElementById(idImg);
    // console.log(imagen);
    imagen.style.background = "rgba(240,150,80,0.5)";
    for(let i=0; i<tamPreguntas; i++){
        if((imgs[i].id!=imagen.id) && (imgs[i].name==imagen.name)){
            imgs[i].style.background = "rgba(0, 0, 0, 0)";
        }
    }
}

function enviaForm(form,opc,m,s,sb){
    // swal("Holi","","info");    
    $("form").submit(function(e){//entro en la funcion submit
    e.preventDefault();//Desactivo el envio automatico
    let objetos = document.querySelectorAll("input[type=radio]:checked");    
    if(objetos.length<opc){
        swal("Te falta responder","Selecciona una imagen de acuerdo a lo que entiendas","warning");
    }else{
        let datos = [];
        objetos.forEach(e => datos.push(e.value));        
        $.ajax({
            url: '/SaveTest',
            type: 'POST',
            data: {
                modulo: m,
                sesion: s,
                submod: sb,
                'arreglo': JSON.stringify(datos) //stringify codifica un arreglo en formato texto jason
            },
            cache:false,
            success: function(response){
                let msj = "";
                let ruta = "";
                if(response=="comic"){
                    msj = "Veamos otra historieta";                    
                    ruta = "/mod"+m+"/sesion"+s+"/subm"+sb+"/retro";
                }
                else{

                    msj = "Pasemos a otro tema";                    
                    if(m==1 && s==1){
                        if(sb>=1 && sb <=4){
                            ruta = "/mod"+m+"/sesion"+s+"/subm"+(++sb);
                        }else{
                            ruta = "/mod1/sesion2/subm1";
                        }
                    }

                    if(m==1 && s==2){
                        if(sb>=1 && sb <=6){
                            ruta = "/mod"+m+"/sesion"+s+"/subm"+(++sb); //Validar el caso 1,2,7 == del comic mandar a la parte de else de este if
                        }else{
                            ruta = "/mod1/sesion1/s-preguntas"; // -> de aqui nos vamos a "/mod1/sesion2/s-video"
                        }
                    }

                    if(m==2 && s==1){
                        if(sb>=1 && sb <=3){
                            ruta = "/mod"+m+"/sesion"+s+"/subm"+(++sb);
                        }else{
                            ruta = "/mod2/sesion2/subm1";
                        }
                    }

                    if(m==2 && s==2){
                        if(sb==1){
                            ruta = "/mod"+m+"/sesion"+s+"/subm"+(++sb);
                        }else if(sb==2){
                            ruta = "/mod1/sesion2/s-preguntas"; // -> de aqui nos vamos a "/mod2/sesion1/s-video"   -> de aqui nos vamos a "/mod2/sesion2/s-preguntas"
                        }
                    }

                    if(m==3 && s==1){
                        if(sb==1){
                            ruta = "/mod3/sesion2/subm1";
                        }
                    }

                    if(m==3 && s==2){
                        if(sb==1){
                            ruta = "/gracias";
                        }
                    }

                }
                swal({
                    title: "¡Muy Bien! :)",
                    text: msj,
                    type: "success"
                    },
                    function(){
                        setTimeout(function(){location.href = ruta;},350);//Esperamos 0.35s para recargar la pagina
                    }
                );
            }
        });
    }

    });
}
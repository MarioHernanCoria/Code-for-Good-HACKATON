    // fetch('../eventos.json')
    // .then((response) => response.json())
    // .then((data) => {
    //     data
    //     .filter(filtrar)
    //     .forEach((evento) => {
    //             let div = document.createElement('div')
    //             div.innerHTML = `
    //             <img src="${evento.img}" class="imgEvento"></img>
    //             <div class="divColumn">
    //                 <p class="tituloNoticia">${evento.Organizacion}</p>
    //                 <p class="noticia">${evento.Nombre_evento}</p>
    //             </div>`
    //             div.classList.add("divJavascript");
    //             let divEventos = document.getElementById("divEventos");
    //             divEventos.appendChild(div);
    //     })
    // })
    const getEventos = () => {
        let divEventos = document.getElementById("divEventos");
        divEventos.innerHTML = "";
        fetch('../eventos.json')
        .then((response) => response.json())
        .then((data) => {
            data
            .filter(categoriaOrganizaciones)
            .forEach((evento) => {
                    let div = document.createElement('div')
                    div.innerHTML = `
                    <img src="${evento.img}" class="imgEvento"></img>
                    <div class="divColumn">
                        <p class="tituloNoticia">${evento.Organizacion}</p>
                        <p class="noticia">${evento.Nombre_evento}</p>
                    </div>`
                    div.classList.add("divJavascript");
                    divEventos = document.getElementById("divEventos");
                    divEventos.appendChild(div);
            })
        })
    }

    let radio1 = document.getElementById("rugby");
    radio1.addEventListener("click", getEventos);
    let radio2 = document.getElementById("tenis");
    radio2.addEventListener("click", getEventos);
    let radio3 = document.getElementById("futbol");
    radio3.addEventListener("click", getEventos);
    let radio4 = document.getElementById("basket");
    radio4.addEventListener("click", getEventos);
    


    const categoriaOrganizaciones = (evento) =>{
        let categoria = (document.querySelector("input[name=categoria]:checked").value)
        return evento.Etiquetas.includes(categoria);
        }



getEventos();

    // const categoriaNutricion = () =>{
    //     let card = document.getElementById('nutricion');
    //     card.classList.add("activo");
    // }




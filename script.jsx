async function buscarUsuario(usuario, contrasena){
    fetch('http://127.0.0.1:8000/test', {
        method: 'POST',
        body: JSON.stringify({
            name: usuario,
            password: contrasena
        }),
        headers: {
            'Content-Type': 'application/json: charset=UTF=8',
        }
    })
    .then((response) => response.json())
    .then((data) => console.log(data))

}

const comprobarUser = (data) =>{
    event.preventDefault();
    let user = document.getElementById('user').value;
    let password = document.getElementById('password').value;
    buscarUsuario(user, password);
}
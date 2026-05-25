const Button1 = document.getElementById("Button1")

async function buscarUsuario() {

    const usuario = document.getElementById("username")
    const resultado = document.getElementById("resultado")

    try{
        const respuestaPerfil = await fetch(`https://api.github.com/users/${usuario.value}`)
        
        if(!respuestaPerfil.ok) throw new Error("Usuario no encontrado")

        const perfil = await respuestaPerfil.json()

        const respuestaRepos = await fetch(`https://api.github.com/users/${usuario.value}/repos`);
        
        const repos = await respuestaRepos.json();

        resultado.innerHTML =` 
            <h2>${perfil.login}</h2>
            <img src="${perfil.avatar_url}" width="100">
            <p>Nombre: ${perfil.name || "No disponible"}</p>
            <p>Bio: ${perfil.bio || "No disponible"}</p>
            <p>Seguidores: ${perfil.followers}</p>
            <p>Siguiendo: ${perfil.following}</p>
            <h3>Repositorios:</h3>
            <ul>
                ${repos.map(repo => `<li><a href="${repo.htm_lurl}" target="blank">${repo.name}</a></li>`).join("")}
            </ul>`
        ;
    } catch (error) {
        resultado.innerHTML = `<p style="color:red;">${error.message}</p>`;
    }
}


Button1.addEventListener("click",buscarUsuario)

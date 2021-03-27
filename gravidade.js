/*function forca_gravitacional() {
    g = 6.674184 * 10 ** -11 // constante gravitacional
    d = 100 //metros        // distancia entre os corpos

    corpo1 = 1000 //massa em quilos
    corpo2 = 200

    tempo = 1_000_000//escala de tempo // múltiplo de 10
    cont_tempo = 0

    while (true) {
        f = g * ((corpo1 * corpo2)/d**2)
        if (d <= 0) {
            break
        }
        else {
            d = d - (tempo*f)
        }
        cont_tempo += 1
        console.log(d)
    }
    corr_tempo = cont_tempo*tempo // correção temporal
}

forca_gravitacional()*/

g = 6.674184 * 10 ** -11 // constante gravitacional
d = 100 //metros        // distancia entre os corpos

corpo1 = 1000 //massa em quilos
corpo2 = 200

tempo = 10_000_000 //escala de tempo // múltiplo de 10
cont_tempo = 0



var c = document.getElementById('tela')
var ctx = c.getContext('2d')


function atualiza() {
    f = g * ((corpo1 * corpo2)/d**2)
    if (d <= 0) {
        return 'Encerra'
    }
    else {
        d = d - (tempo*f)
    }
    cont_tempo += 1
    console.log(d)
    return d
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function desenha() {
    atualiza()
    if (d <= 0) {return 'Encerra'}
    //x1 = 200 + (-d)
    //x2 = 800 - (-d)
    x1 = ((-d*3)+500) //3 = escala
    x2 = ((d*3)+500)
    ctx.beginPath()
    ctx.arc(x1,276,20,0,Math.PI * 2)
    ctx.fillStyle = 'red'
    ctx.fill()
    ctx.closePath()

    ctx.beginPath()
    ctx.arc(x2,276,20,0,Math.PI * 2)
    ctx.fillStyle = 'red'
    ctx.fill()
    ctx.closePath()
    
}


function roda () {
    desenha()
    setInterval(roda, 60) //15 = 60FPS, 30 = 30FPS, 60 = 15FPS
}

function reset() {
    location.reload()
}




// Navbar Scroll

window.addEventListener('scroll', function(){

    const navbar = document.querySelector('.custom-navbar');

    if(window.scrollY > 50){
        navbar.style.background = "rgba(8,17,32,0.95)";
    }else{
        navbar.style.background = "rgba(8,17,32,0.8)";
    }

});

// Orb Parallax

document.addEventListener('mousemove', (e)=>{

    const orbs = document.querySelectorAll('.orb');

    const x = e.clientX / window.innerWidth;
    const y = e.clientY / window.innerHeight;

    orbs.forEach((orb,index)=>{

        const speed = (index + 1) * 20;

        orb.style.transform =
            `translate(${x * speed}px, ${y * speed}px)`;

    });

});
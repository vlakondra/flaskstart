$(function () {
    let opt = {
        loop: false,
        nav: true,
        autoWidth: true,
        margin: 10,
        responsive: false,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: true,
                loop: true
            },
            600: {
                items: 3,
                nav: false
            },
            1000: {
                items: 5,
                nav: true,
                loop: false
            }
        }
    }

    var OWL = $(".owl-carousel").owlCarousel(opt);

    OWL.on('dragged.owl.carousel', function (event) {
        console.log('dragged!')

    })

})
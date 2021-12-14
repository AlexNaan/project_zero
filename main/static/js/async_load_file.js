window.addEventListener("load", load_page);
function load_page() {


    loadPhotoEmployee();

    loadCertificateEmploy();


}

function loadPhotoEmployee() {

    let pathArray = document.location.pathname.split('/');
    let codeEmployee = pathArray[pathArray.length - 2];



    let formData = new FormData();
    formData.append("code_employee", codeEmployee);
    formData.append("Type", "Photo");


    fetch(`http://localhost:8000/api/photo/${codeEmployee}`)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            let photo_employee = document.querySelector("#Photo_employee")
            photo_employee.src = "/" + data.pathPhoto
        });
}

function loadCertificateEmploy() {

    let ArrayCertificate = document.querySelectorAll(".Certificate");


    ArrayCertificate.forEach((certificate)=> {
        
        fetch(`http://localhost:8000/api/certificate/${certificate.id}`)
            .then((response) => {
                return response.json();
            })
            .then((dataCertificate) => {
                let idCertificate = dataCertificate.id
                let urlCertificate = dataCertificate.url

                if (urlCertificate !== '#') {
                    /*
                        удалим span на его место поставим ссылку
                    */
                    let parent = certificate.parentNode;
                    let titltCertificate = certificate.innerHTML;
                    parent.removeChild(certificate);

                    let hrefCertificate = document.createElement('a');
                    hrefCertificate.href = urlCertificate;
                    hrefCertificate.innerHTML = titltCertificate;
                    parent.append(hrefCertificate);
                }
            });
    });
}
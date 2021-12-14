

window.addEventListener('load', afterLoad)


function afterLoad(){

    let inSearch = document.querySelector('#searchEmployee')
    inSearch.addEventListener('keypress',startSearch)

}

function startSearch(event){
    if (event.keyCode == 13) {
        let emp = event.target.value.toUpperCase()
        let arraySearch = []
        document.querySelector('tbody').querySelectorAll('a').forEach(el=>{
            if (el.innerText.toUpperCase().indexOf(emp) != -1){
                /*Удалим у родителя оформление*/
				el.offsetParent.parentNode.classList.remove('selectRow')

				let info = {
                    id:el.dataset.idData,
                    name:el.innerText
                }
                arraySearch.push(info)
            }
        })

	    let listSearch = document.querySelector('.listSearch')
		listSearch.classList.remove('searchNone')
		parentUL = listSearch.querySelector('ul')
		while (parentUL.firstChild) {
			parentUL.removeChild(parentUL.firstChild);
		}

		arraySearch.forEach(rezult=>{

			let el_ = document.createElement('li');
			let linkE = document.createElement('a');

			linkE.setAttribute('idLink',rezult.id)
			linkE.addEventListener('click',function(e){
				idEmp = e.target.getAttribute('idLink')
				let emmloyee = document.getElementById(idEmp);
				emmloyee.classList.add('selectRow')
                listSearch.classList.add('searchNone')
			})
			
			linkE.href = "#" + rezult.id
			linkE.innerHTML = rezult.name
			el_.append(linkE)
			
			
			parentUL.append(el_)
		})
    }


}

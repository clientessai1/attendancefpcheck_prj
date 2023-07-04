var path_name = window.location.pathname;
//Tableau associatif
var url_and_id_assoc_array = {
'/':'id_link_home',
'/entree':'id_link_entree',
'/sortie':'id_link_sortie'
};

for (var key in url_and_id_assoc_array)
{

 if (path_name == key)
 {
 
   var link_id = url_and_id_assoc_array[key];
   //Get collection of element with scrollto class
   var collection = document.getElementsByClassName("scrollto");
   var taille = collection.length;
   //Remove active class from all the upper collection elements   
   for(let i=0; i < taille; i++)
   {
     collection[i].classList.remove('active');
   }

   //Add active class to the current id element.
   a_element = document.getElementById(link_id);
   a_element.classList.add('active');
   break;

 }
 
}

// Récupérer la liste des classes scrollto

//Enlever la classe active de toutes les classes scrollto

//Ajouter la classe active à l'élément dont l'id à une correspondance avec la page chargée.


//alert(path_name);

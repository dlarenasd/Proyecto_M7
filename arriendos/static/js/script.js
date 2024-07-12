const filtrarComunas = async (regionId) => {
    const csrfTokenValue = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    ).value;
    const headers = {
      "X-CSRFToken": csrfTokenValue,
    };
  
    let url = "/filtrar-comunas/"; 
    try {
      const response = await axios.post(url, { regionId }, { headers });
  
      //console.log(response);
      const { data, status } = response;
  
      if (status == 200) {
        let selectComunas = document.querySelector("#comunas");
        selectComunas.innerHTML = "";
  
        // Crea una opción por defecto
        const defaultOption = document.createElement("option");
        defaultOption.value = "0";
        defaultOption.text = "Seleccione una comuna";
        selectComunas.appendChild(defaultOption);
  
        // Itera sobre la data para agregar las comunas al select
        data.data.forEach((item) => {
          const option = document.createElement("option");
          option.value = item.id;
          option.text = item.nombre;
          selectComunas.appendChild(option);
        });
      } else {
        console.log("No hay comunas disponibles");
      }
    } catch (error) {
      console.log("Error en la petición", error);
    }
  };
  
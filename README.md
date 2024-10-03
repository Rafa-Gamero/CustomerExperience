# Análisis A/B para Vanguard.

## Introducción

Bienvenidos al proyecto de Análisis A/B de Experiencia del Usuario (Vanguard), una empresa de gestión de inversiones con sede en EE.UU. En este proyecto, se evalúa la efectividad de una nueva interfaz de usuario (UI) y los mensajes contextuales en la plataforma digital de Vanguard. El objetivo principal es determinar si estos cambios mejoraron las tasas de finalización del proceso en comparación con la interfaz tradicional.

# Conjuntos de datos del proyecto

El análisis se basa en tres conjuntos de datos principales:

1. **Client Profiles (`df_final_demo`)**: Información demográfica de los clientes, como edad, género, y detalles de la cuenta.
   - [df_final_demo](https://github.com/data-bootcamp-v4/lessons/blob/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_demo.txt)
2. **Digital Footprints (`df_final_web_data`)**: Rastro detallado de las interacciones en línea de los clientes, dividido en dos partes (`pt_1` y `pt_2`), que se combinaron para el análisis.
   - [pt_1](https://github.com/data-bootcamp-v4/lessons/blob/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_web_data_pt_1.txt)
   - [pt_2](https://github.com/data-bootcamp-v4/lessons/blob/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_web_data_pt_2.txt)
3. **Experiment Roster (`df_final_experiment_clients`)**: Lista de clientes que participaron en el experimento, identificando si pertenecen al Grupo de Control o al Grupo de Prueba.
   - [df_final_experiment_clients](https://github.com/data-bootcamp-v4/lessons/blob/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_experiment_clients.txt)

## Metodología

El experimento se llevó a cabo del 15 de marzo de 2017 al 20 de junio de 2017. Los clientes fueron divididos en dos grupos:

- **Grupo de Control**: Interactuaron con el proceso en línea tradicional.
- **Grupo de Prueba**: Experimentaron la nueva interfaz digital.

### Hipótesis

1. **Hipótesis 1: La nueva interfaz aumentará la tasa de finalización del proceso.**
   - **Prueba Realizada**: Comparación de las tasas de finalización entre el Grupo de Control y el Grupo de Prueba.
   - **Conclusión**: La tasa de finalización en el Grupo de Prueba fue significativamente mayor en comparación con el Grupo de Control. Esto sugiere que la nueva interfaz fue efectiva para aumentar las tasas de finalización del proceso.

2. **Hipótesis 2: Los clientes con una mayor antigüedad con Vanguard tienen una mayor probabilidad de completar el proceso.**
   - **Prueba Realizada**: Análisis de la relación entre la antigüedad del cliente y la tasa de finalización, controlando el grupo de prueba/control.
   - **Conclusión**: No se encontró una relación significativa entre la antigüedad del cliente y la tasa de finalización. Esto indica que la antigüedad con Vanguard no influyó notablemente en la probabilidad de completar el proceso en el contexto del experimento.

3. **Hipótesis 3: La nueva interfaz es más efectiva para clientes con una alta frecuencia de inicio de sesión en los últimos seis meses.**
   - **Prueba Realizada**: Comparación de la tasa de finalización entre clientes con alta y baja frecuencia de inicio de sesión, diferenciando entre el Grupo de Control y el Grupo de Prueba.
   - **Conclusión**: Los clientes con alta frecuencia de inicio de sesión mostraron una mayor tasa de finalización en el Grupo de Prueba en comparación con el Grupo de Control. Esto sugiere que la nueva interfaz fue más efectiva para clientes que ya están muy involucrados en la plataforma.

## Resultados

- **Métricas de Desempeño**: La nueva interfaz demostró una mejora significativa en las tasas de finalización del proceso.
- **Evaluación del Experimento**: El diseño del experimento fue adecuado, pero la duración podría haber sido extendida para capturar un mayor número de interacciones.

## Visualizaciones

Las visualizaciones interactivas creadas en Tableu ofrecen una visión clara del impacto de la nueva interfaz. Puedes explorar el dashboard [aquí](https://public.tableau.com/app/profile/rafael.gamero.arrabal/viz/DasboardABVanguar/Dashboard1?publish=yes).

## Conclusión

El análisis indica que la nueva interfaz digital de Vanguard es más efectiva en términos de tasas de finalización del proceso. Aunque la antigüedad del cliente no mostró un impacto significativo, la frecuencia de inicio de sesión y la nueva interfaz demostraron una relación positiva. Se recomienda continuar con la implementación de la nueva interfaz y considerar una extensión en la duración del experimento para obtener resultados más robustos.

## Enlaces

- [Repositorio en GitHub](https://github.com/Rafa-Gamero/vanguard-ab-test)
- [Tablero Kanban en Trello](https://trello.com/b/DZwyxiRR/proyecto-2)
- [Diapositivas de la Presentación](https://docs.google.com/presentation/d/14_VSmUI-jnBwQWAVEkyppwFnhZsuXOs0I3DVEJgN3Fs/edit#slide=id.g307e4d75c01_0_28)
- [Dashboard en Tableu](https://public.tableau.com/app/profile/rafael.gamero.arrabal/viz/DasboardABVanguar/Dashboard1?publish=yes)

## Contacto

Para cualquier pregunta o comentario sobre este proyecto, no dudes en contactarnos.

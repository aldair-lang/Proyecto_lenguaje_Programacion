% Recibe argumentos desde consola: swipl -q -s razonador.pl -g "evaluar(alto, si, no, cerrado, si, si)" -t halt

evaluar(Consumo, CableAntiguo, Estabilizador, Espacio, Humedad, Ausente) :-
    deducir_alertas(Consumo, CableAntiguo, Estabilizador, Espacio, Humedad, Ausente).

deducir_alertas(alto, si, _, _, _, _) :-
    writeln('ALERTA: Sobrecarga severa inminente por alta demanda en cableado antiguo.'),
    writeln('ACCION: Distribuir cargas en circuitos independientes y revisar llaves termicas.'),
    fail.

deducir_alertas(alto, _, no, _, _, _) :-
    writeln('ALERTA: Equipos de alto consumo operando sin supresor ni estabilizador.'),
    writeln('ACCION: Instalar regulador de voltaje para evitar danos por picos.'),
    fail.

deducir_alertas(_, _, _, cerrado, si, _) :-
    writeln('ALERTA: Riesgo de condensacion y sulfatacion en conexiones por humedad.'),
    writeln('ACCION: Ventilar el area o usar deshumidificador.'),
    fail.

deducir_alertas(Consumo, _, _, _, _, si) :-
    Consumo \= bajo,
    writeln('ALERTA: Cargas electricas activas sin supervision humana en el predio.'),
    writeln('ACCION: Desconectar equipos no esenciales antes de salir.'),
    fail.

% Regla de cierre cuando termina de revisar todas las combinaciones
deducir_alertas(_, _, _, _, _, _).
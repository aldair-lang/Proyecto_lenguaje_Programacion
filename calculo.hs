import System.Environment (getArgs)

-- Funciones puras de ponderacion
pesoElectrico :: String -> String -> String -> Int
pesoElectrico "alto" "si" _    = 40
pesoElectrico "alto" _    "no" = 25
pesoElectrico "medio" "si" _   = 20
pesoElectrico _ _ _            = 0

pesoAmbiental :: String -> String -> Int
pesoAmbiental "cerrado" "si" = 30
pesoAmbiental "cerrado" _    = 15
pesoAmbiental _ "si"         = 15
pesoAmbiental _ _            = 0

pesoHabito :: String -> String -> Int
pesoHabito consumo "si" | consumo /= "bajo" = 20
pesoHabito _ _                              = 0

clasificarRiesgo :: Int -> String
clasificarRiesgo pts
    | pts >= 50 = "CRITICO (Accion Inmediata)"
    | pts >= 25 = "MODERADO (Atencion Preventiva)"
    | otherwise = "SEGURO (Bajo Control)"

main :: IO ()
main = do
    args <- getArgs
    case args of
        [consumo, antiguo, estab, espacio, humedad, ausente] -> do
            let total = min 100 (pesoElectrico consumo antiguo estab + pesoAmbiental espacio humedad + pesoHabito consumo ausente)
            putStrLn $ show total ++ "|" ++ clasificarRiesgo total
        _ -> putStrLn "0|Error en parametros"
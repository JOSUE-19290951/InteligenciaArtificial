package AI;

public class PerceptionOr {

    public static void main(String[] args) {
        int datos[][] = {{0, 0, 0, 1},{0, 0, 1, 1},{0, 1, 0, 1},{0, 1, 1, 1}, {1, 0, 0, 1}, {1, 0, 1, 1}, {1, 1, 0,1},{1, 1, 1, 1}};
        double pesos[] = {Math.random() * 10, Math.random() * 10, Math.random() * 10, Math.random()*10};
        int salidas[]={0,0,0,0,0,0,0,1};
        int salida = 0;
        boolean aprendiendo = true;
        double tasaA = 0.3;
        int sumatoria = 0;
        while (aprendiendo) {
            aprendiendo = false;
            for (int cont = 0; cont < datos.length; cont++) {
                double salidaR = datos[cont][0] * pesos[0] + datos[cont][1] * pesos[1] + datos[cont][2] * pesos[2]+datos[cont][3]*pesos[3];
                if (salidaR > 0) {
                    salida = 1;
                } else {
                    salida = 0;
                }
                int error = datos[cont][3]-salida;
                error = salidas[cont]-salida;
                /*if (salida != datos[cont][2]) {
                    pesos[0] = Math.random() * 10 - Math.random() * 10;
                    pesos[1] = Math.random() * 10 - Math.random() * 10;
                    pesos[2] = Math.random() * 10 - Math.random() * 10;
                    System.out.println("Entrenando");
                    aprendiendo = true;
                }*/
                if(error != 0){
                    pesos[0] += tasaA * error * datos[cont][0];
                    pesos[1] += tasaA * error * datos[cont][1];
                    pesos[2] += tasaA * error * datos[cont][2];
                    pesos[3] += tasaA * error * datos[cont][3];
                    aprendiendo = true;
                }
                for(int i=0; i<pesos.length; i++){
                    sumatoria += datos[cont][i]*pesos[i];
                    salidaR = 1/(Math.exp(-sumatoria));
                }
            }
            Pesos.establecerPesos(pesos, "pesosOrA.txt");
        }
        for (int cont = 0; cont < datos.length; cont++) {
            double salidaR = datos[cont][0] * pesos[0] + datos[cont][1] * pesos[1] + datos[cont][2] * pesos[2] + datos[cont][3]*pesos[3];
            if (salidaR > 0) {
                salida = 1;
            } else {
                salida = 0;
            }
            System.out.println(datos[cont][0] + "," + datos[cont][1] + "," + datos[cont][2] +"," +datos[cont][3]+", perception =" + salida);
        }
        System.out.println("");
    }
}

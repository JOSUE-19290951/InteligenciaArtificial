
package AI;
import java.util.*;

public class PruebaPerceptionOr {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x1, x2, x3, salida;
        double salidaR;
        double[] pesos = new double[4];
        pesos = Pesos.obtenerPesos(pesos, "pesosOrA.txt");
        System.out.print("Dame entrada 1: ");
        x1 = sc.nextInt();
        System.out.print("Dame entrada 2: ");
        x2 = sc.nextInt();
        System.out.print("Dame entrada 3: ");
        x3 = sc.nextInt();
        salidaR = x1*pesos[0]+x2*pesos[1]+x3*pesos[2]+pesos[3];
        System.out.println(salidaR);
        if(salidaR<0){
            salida = 0;
        }
        else{
            salida = 1;
        }
        System.out.println(x1+" , "+x2+", "+x3+" = "+salida);
    }
}

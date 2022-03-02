package AI;
import java.io.*;
    
public class Pesos {
    public static double [] obtenerPesos(double[] pesos, String archivo){
        BufferedReader ent;
        try{
            ent = new BufferedReader(new FileReader(new File(archivo)));
            for(int i=0; i<pesos.length; i++){
                pesos[i]= Double.parseDouble(ent.readLine());
            }
            ent.close();
        }
        catch(IOException e){
        }
        return pesos;
    }
    public static void establecerPesos(double pesos[], String archivo){
        PrintWriter sal;
        try{
            sal = new PrintWriter(new FileWriter(new File(archivo)));
            for(int i =0; i<pesos.length; i++){
                sal.println(pesos[i]);
            }
            sal.close();
        }catch(IOException e){
        }
    }
}

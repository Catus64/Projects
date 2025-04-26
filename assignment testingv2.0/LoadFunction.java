import java.io.BufferedReader;
import java.io.FileReader;
/**
    @author Wan Abdul Rahman
 */
public class LoadFunction
{
 


    public LoadFunction() 
    {
    }
    
    public void loadGame(BoardLogicModel BML) throws java.io.FileNotFoundException
    {
        BufferedReader reader = new BufferedReader(new FileReader("Savefile/Output.txt"));
        try
        {
            String turn = reader.readLine();
            int t = Integer.parseInt(turn);
            BML.turnLoad = t;
            //System.out.println(t +" HAHA");
            
            String line;
            
            while((line = reader.readLine())!=null)
            {
                String[] temp = line.split(",");
                String team;
                //System.out.println(line);
                System.out.println(temp[0]);
                System.out.println(temp[1]);
                System.out.println(temp[2]);
                System.out.println(temp[3]);
                if(temp[3].equals("blue"))
                {
                    team = "blue";
                }else{team = "red";}
                
                int x = Integer.parseInt(temp[1]);
                int y = Integer.parseInt(temp[2]);
                
                if(temp[0].equals("Ram"))
                {
                System.out.println("A "+ temp[3] + "RAM is here");
                BML.pieces[y][x] = new Ram(x,y,team);
                }
                else if(temp[0].equals("Xor"))
                {
                System.out.println("A "+ temp[3] + "XOR is here");
                BML.pieces[y][x] = new Xor(x,y,team);
                }
                else if(temp[0].equals("Sau"))
                {
                BML.pieces[y][x] = new Sau(x,y,team);
                }
                else if(temp[0].equals("Biz"))
                {
                    System.out.println("A "+ temp[3] + "BIZ is here");
                BML.pieces[y][x] = new Biz(x,y,team);
                }
                else if(temp[0].equals("Tor"))
                {
                BML.pieces[y][x] = new Tor(x,y,team);
                }
            }
            reader.close();
        }
        catch (java.io.IOException ioe)
        {
            ioe.printStackTrace();
        }
        
    }
}

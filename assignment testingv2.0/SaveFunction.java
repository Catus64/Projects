
import java.io.File; 
import java.io.IOException;
import java.io.FileWriter;  
import java.io.BufferedWriter;

/**
    @author Wan Abdul Rahman
 */

public class SaveFunction
{
 
    public SaveFunction()
    {
     //File saveFile = new File("save.txt");
    }


    public void SaveGame(BoardLogicModel BML,int turn) throws IOException
    {
        try{
        BufferedWriter writer = new BufferedWriter(new FileWriter("Savefile/Output.txt"));
        
        //System.out.println(turn);
        writer.write(""+turn);
        for(int i = 0; i < 8;i++){
            for(int j=0; j<5;j++){
                if(BML.isOccupied(j,i))
                {
                    //if(j==0 && i == 0){
                    //writer.write(BML.pieces[i][j].type+","+j+","+i+","+BML.pieces[i][j].team);
                    //}else
                    //{
                    writer.write("\n" + BML.pieces[i][j].type+","+j+","+i+","+BML.pieces[i][j].team);
                    //}
                }
            }
        }
        
        writer.close();
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}


/**
    @author Wan Abdul Rahman
    Implementation of the Sau Piece
 */
public class Sau extends Piece
{
    int[] algX = {-1,-1,-1,0,0,1,1,1};
    int[] algY= {-1,0,1,-1,1,-1,-1,0,1};
    int tempX,tempY;

    /**
     * Constructor for objects of class Sau
     */
    public Sau(int x,int y, String team_select)
    {
        super.type = "Sau";
        super.is_alive = true;
        super.is_red = false;
        super.posX = x;
        super.posY = y;
        super.team = team_select;
    }


    @Override
    public void pieceMovement(BoardLogicModel BML)
    {
        System.out.println("Xor is moving at (" +posX +","+posY);
        //up left

        for(int j = 0;j < 8;j++){
        tempX = posX;
        tempY = posY;
        System.out.println("Turning");
        //for(int i = 0; i < 3 ;i++)
        //{   
            super.nextX = tempX + algX[j];
            super.nextY = tempY + algY[j];
            System.out.println("Checking (" +nextX +","+nextY);
            if(!BML.inBounds(nextX,nextY)){continue;}
            if(!BML.isOccupied(nextX,nextY))
            {
                System.out.println("Tile is available at ("+ nextX+" "+nextY+" )");
                BML.pieces[nextY][nextX].pieceMovement(BML);
                System.out.println(BML.pieces[nextY][nextX].team);
            }else{
                System.out.println("KILL");
                BML.isKillable(nextX,nextY,this);
                continue;
            }
            //tempX = nextX;
            //tempY = nextY;
        
        //}
        }
    }
}

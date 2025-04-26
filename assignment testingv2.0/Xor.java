
/**
    @author Wan Abdul Rahman
    Implementation of the Xor Piece
 */
public class Xor extends Piece
{
    
    int[] algX = {-1,1,1,-1};
    int[] algY= {-1,-1,1,1};
    int tempX,tempY;
    /**
     * Constructor for objects of class Biz
     */
    public Xor(int x,int y, String team_select)
    {
        super.type = "Xor";
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

        for(int j = 0;j < 4;j++){
        tempX = posX;
        tempY = posY;
        System.out.println("Turning");
        for(int i = 0; i < 5 ;i++)
        {   
            super.nextX = tempX + algX[j];
            super.nextY = tempY + algY[j];
            System.out.println("Checking (" +nextX +","+nextY);
            if(!BML.inBounds(nextX,nextY)){break;}
            if(!BML.isOccupied(nextX,nextY))
            {
                System.out.println("Tile is available at ("+ nextX+" "+nextY+" )");
                BML.pieces[nextY][nextX].pieceMovement(BML);
                System.out.println(BML.pieces[nextY][nextX].team);
            }else{
                System.out.println("KILL");
                BML.isKillable(nextX,nextY,this);
                break;
            }
            tempX = nextX;
            tempY = nextY;
        
        }
        }
    }
}

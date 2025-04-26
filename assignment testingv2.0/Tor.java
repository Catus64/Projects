
/**
    @author Wan Abdul Rahman
    Implementation of the Tor Piece
 */
public class Tor extends Piece
{
    
    int[] algX = {1,0,-1,0};
    int[] algY= {0,1,0,-1};
    int tempX,tempY;

    /**
     * Constructor for objects of class Tor
     */
    public Tor(int x,int y, String team_select)
    {
        super.type = "Tor";
        super.is_alive = true;
        super.is_red = false;
        super.posX = x;
        super.posY = y;
        super.team = team_select;
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    @Override
    public void pieceMovement(BoardLogicModel BML)
    {
        System.out.println("Xor is moving at (" +posX +","+posY);
        //up left

        for(int j = 0;j < 4;j++){
        tempX = posX;
        tempY = posY;
        System.out.println("Turning");
        for(int i = 0; i < 7 ;i++)
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

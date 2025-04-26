
/**
    @author Wan Abdul Rahman
    Implementation of the Ram Piece
 */
public class Ram extends Piece
{
    String movesLike;
    boolean flipping;
    public Ram(int x,int y, String team_select)
    {
        super.type = "Ram";
        movesLike = team_select;
        super.is_alive = true;
        super.is_red = false;
        super.posX = x;
        super.posY = y;
        flip = false;
        super.team = team_select;
    }
    
    @Override
    public void pieceMovement(BoardLogicModel BML)
    {
        System.out.println("Ram is moving");
        boolean pass = false;
        
        while(!pass){
            if(movesLike == "blue"){
                System.out.println("Blue Ram is moving");
                super.nextX = super.posX;
                super.nextY = super.posY - 1;
            }else if(movesLike == "red"){
                System.out.println("red Ram is moving");
                super.nextX = super.posX;
                super.nextY = super.posY + 1;
                }
            if(ramFlip(nextX,nextY,BML)){continue;}
            pass = true;
            flipping = false;
            }
            System.out.println("Tile is available at ("+ nextX+" "+nextY+" )");
        if(!BML.isOccupied(nextX,nextY)){
                System.out.println("Tile is available at ("+ nextX+" "+nextY+" )");
                BML.pieces[nextY][nextX].pieceMovement(BML);
                System.out.println(BML.pieces[nextY][nextX].team);
                }
            else
            {
                BML.isKillable(nextX,nextY,this);
            }
        }
    public boolean ramFlip(int x,int y,BoardLogicModel BML)
    {
        if(flipping){return true;}
        if(!BML.inBounds(nextX,nextY))
        {
            flip ^= true;
            if(movesLike == "red"){movesLike = "blue";}
            else if(movesLike == "blue"){movesLike = "red";}
            flipping = true;
        }
        return false;
    }
}

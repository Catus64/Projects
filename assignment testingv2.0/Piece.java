import javax.swing.ImageIcon;

/**
    @author Wan Abdul Rahman
    This is an abstract class for other pieces
    it contains the basic attributes like positions and if its flipped.
 */
public abstract class Piece
{
    protected String team,type;
    protected boolean is_alive,is_red,flip;
    protected int posX,posY;
    protected int nextX,nextY;
    
    public Piece()
    {

    }
    
    public void targeted()
    {
        is_red = true;    
    }
    public void unTarget()
    {
        is_red = false;
    }
    public void dead()
    {
        is_alive = false;
    }
    
    public abstract void pieceMovement(BoardLogicModel BML);
    

}

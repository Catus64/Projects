
/**
 * The main Processing Brain for the game
 *
 *
 * @author 
 *         Wan Abdul Rahman
 *
 */
public class BoardLogicModel
{
    Piece[][] pieces;
    LoadFunction load = new LoadFunction();
    int turnLoad;
    
    public BoardLogicModel()
    {
         
         pieces = new Piece[8][5];
         
         for(int i = 0; i<8;i++){
             for(int j = 0;j <5;j++){
                pieces[i][j] = new Tile(i,j);
                }
         }
         //pieces[6][0] = null;
         pieces[0][0] = new Xor(0,0,"red");
         pieces[0][1] = new Biz(1,0,"red");
         pieces[0][2] = new Sau(2,0,"red");
         pieces[0][3] = new Biz(3,0,"red");
         pieces[0][4] = new Tor(4,0,"red");
         
         pieces[1][0] = new Ram(0,1,"red");
         pieces[1][1] = new Ram(1,1,"red");
         pieces[1][2] = new Ram(2,1,"red");
         pieces[1][3] = new Ram(3,1,"red");
         pieces[1][4] = new Ram(4,1,"red");
         
         pieces[6][0] = new Ram(0,6,"blue");
         pieces[6][1] = new Ram(1,6,"blue");
         pieces[6][2] = new Ram(2,6,"blue");
         pieces[6][3] = new Ram(3,6,"blue");
         pieces[6][4] = new Ram(4,6,"blue");
         
         pieces[7][0] = new Tor(0,7,"blue");
         pieces[7][1] = new Biz(1,7,"blue");
         pieces[7][2] = new Sau(2,7,"blue");
         pieces[7][3] = new Biz(3,7,"blue");
         pieces[7][4] = new Xor(4,7,"blue");
    }
    
    public void loadGameLogic()
    {
         pieces = new Piece[8][5];
         
         for(int i = 0; i<8;i++){
             for(int j = 0;j <5;j++){
                pieces[i][j] = new Tile(i,j);
                }
         }
         try
         {
             load.loadGame(this);
         }
         catch (java.io.FileNotFoundException fnfe)
         {
             fnfe.printStackTrace();
         }
    }
    
    public String getPieceType(int x,int y)
        {
            return pieces[y][x].type;
        }
    public String getTeam(int x,int y)
        {
            return pieces[y][x].team;
        }
    public boolean isOccupied(int x,int y)
        {
         if(pieces[y][x].type.equals(("Tile")))
            {
            return false;
            }else{
            return true;
            }
        
        }
    public void isKillable(int x,int y,Piece P)
        {
            if(pieces[y][x].team != P.team)
            {
             pieces[y][x].targeted();
            }
        }
    public void clearGreen(BoardView bView)
    {
        for(int i = 0;i<8;i++){
            for(int j=0;j<5;j++){
            if(pieces[i][j].type == "Tile"){
                pieces[i][j].team = "null";
                bView.resetTile(j,i);
                }
            }
        }
    }
    public void clearTarget(BoardView bView)
    {
        for(int i = 0;i<8;i++){
            for(int j=0;j<5;j++){
            if(pieces[i][j].team != "Tile"){
                pieces[i][j].unTarget();
                bView.clearTarget(j,i);
                }
            }
        }
    }
    public void clearRed(BoardView bView)
    {
        for(int i = 0;i<8;i++){
            for(int j=0;j<5;j++){
            if(pieces[i][j].type == "Tile"){
                pieces[i][j].unTarget();
                bView.resetTile(j,i);
                }
            }
        }
    }
    public void movePiece(int nextX,int nextY,Piece P,BoardView bView)
    {
        pieces[P.posY][P.posX] = new Tile(P.posX,P.posY);
        bView.resetTile(P.posX,P.posY);
        bView.resetTile(nextX,nextY);
        P.posX = nextX;
        P.posY = nextY;
        pieces[nextY][nextX] = P;
        bView.setPiece(nextX,nextY,P.type,P.team);
        
    }
    public void killPiece(Piece Target,Piece P,BoardView bView)
    {
        Target.dead();
        movePiece(Target.posX,Target.posY,P,bView);
    
    
    }
    public boolean inBounds(int x,int y)
    {
        if(x > 4 || x < 0)
        {
            return false;
        }else if(y > 7 || y < 0)
        {
            return false;
        }
        else{return true;}
    }

}

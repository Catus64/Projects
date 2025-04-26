import javax.swing.JOptionPane;
/**
 * @author Agilan a/l Khali Thasan
 *  Wan Abdul Rahman
 *  
 * Process the input and the main structure of controlling the game.  
 *  
 */

public class Controller
{
    int selectX,selectY,turn,moveNum;
    pieceObserver pieceOb;
    Piece temp;
    
    private int x;

    public Controller()
    {
        pieceOb = new pieceObserver();
        turn = 1;
        moveNum = 0;
    }

    public void select(int x,int y,BoardView bView,BoardLogicModel BML,View view){//giving position
        //do the move
        selectX = x;
        selectY = y;
        System.out.println("("+x+","+y+")");
        UpdateGame(x,y,BML,bView,view);
    }
    
    public void startGame(BoardLogicModel BML,View v){
        v.NoMenu();
        v.gameBoard();
        v.boardView.initialize(BML);
        v.BoardSetting();
    }
    
    public void loadGame(BoardLogicModel BML,View v){
        v.NoMenu();
        v.gameBoard();
        BML.loadGameLogic();
        v.boardView.initialize(BML);
        turn = BML.turnLoad;
        updateTurn(v,BML,v.boardView);
        v.BoardSetting();
    }
    
    public void UpdateGame(int x,int y,BoardLogicModel BML,BoardView bView,View view){
        //if a piece is pressed
        if(BML.getPieceType(x,y) == "Tile")
        {//check for moves
         if(BML.pieces[y][x].team == "green")
            {
                BML.movePiece(x,y,BML.pieces[pieceOb.currentY][pieceOb.currentX],bView);
                pieceOb.unlock();
                BML.clearGreen(bView);
                pieceOb.switchTeam();
                BML.clearTarget(bView);
                bView.flipBoard(BML);
                //turn++;
                moveNum++;
                updateTurn(view,BML,bView);
                return;
            }
         System.out.println(" Tile is here "+BML.pieces[y][x].team);
         return;
        }
        System.out.println(BML.pieces[y][x].is_red);
         if(BML.pieces[y][x].is_red)
         {
            System.out.println("Killing...");
            if(BML.pieces[y][x].type == "Sau" )
            {
                System.out.println("GAME WIN");
                view.winNotif(BML.pieces[y][x].team);
                return;
            }
            BML.killPiece(BML.pieces[y][x],BML.pieces[pieceOb.currentY][pieceOb.currentX],bView);
            pieceOb.unlock();
            BML.clearTarget(bView);
            BML.clearGreen(bView);
            pieceOb.switchTeam();  
            bView.flipBoard(BML);
            //turn++;
            moveNum++;
            updateTurn(view,BML,bView);
            return;
         }
        if(!pieceOb.teamcheck(BML.pieces[y][x]))
        {
            System.out.println("Wrong Team");
            return;
        }
        //check if a piece is deselected
        if(pieceOb.checkLock(x,y))
        {
            System.out.println("piece deselected");
            BML.clearGreen(bView);
            BML.clearTarget(bView);
            bView.clearTarget(x,y);
            return;
        }
        //check if piece is selected
        if(pieceOb.isLock())
        {
            System.out.println("deselect piece first");
            return;
        }
        //detect what is pressed
        System.out.println("piece select");
        bView.setTileYellow(x,y);
        System.out.println("There is a "+BML.getPieceType(x,y)+" Here");
        //get movements 
        BML.pieces[y][x].pieceMovement(BML);
        //toggle lock until piece move
        pieceOb.toggle();
        pieceOb.setLock(x,y);
        //highlight green
        //System.out.println(BML.pieces[y][x].team)
        for(int i= 0 ; i < 8;i++){
            for(int j=0 ;j < 5; j++){
                if(BML.pieces[i][j].team.equals("green"))
                {
                    System.out.println("BVEIEW is working");
                    bView.setTileGreen(j,i);
                }
            }
        }
        //if a piece is already pressed
        
        //move the piece
    
        //Target Pieces
        for(int i= 0 ; i < 8;i++){
            for(int j=0 ;j < 5; j++){
                if(BML.pieces[i][j].is_red)
                {
                    //System.out.println("BVEIEW is working");
                    bView.setTileRed(j,i);
                }
            }
        }
    }
    
    public void updateTurn(View v,BoardLogicModel BML,BoardView bView){
        if(moveNum == 2)
        {
            turn ++;
            moveNum = 0;
        }
        if(turn == 2)
        {
            for(int i = 0; i < 8;i++){
                for(int j=0; j<5;j++){
                if(BML.pieces[i][j].type == "Tor"){
                temp = new Xor(BML.pieces[i][j].posX,BML.pieces[i][j].posY,BML.pieces[i][j].team);
                BML.pieces[i][j] = temp;
                BML.movePiece(BML.pieces[i][j].posX,BML.pieces[i][j].posY,BML.pieces[BML.pieces[i][j].posY][BML.pieces[i][j].posX],bView);
                }else if(BML.pieces[i][j].type == "Xor")
                {
                temp = new Tor(BML.pieces[i][j].posX,BML.pieces[i][j].posY,BML.pieces[i][j].team);
                BML.pieces[i][j] = temp;
                BML.movePiece(BML.pieces[i][j].posX,BML.pieces[i][j].posY,BML.pieces[BML.pieces[i][j].posY][BML.pieces[i][j].posX],bView);
                }
            }
            }
        }
        v.boardSettings.updateTurn(turn);
    }
    
}

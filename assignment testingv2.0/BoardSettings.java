import javax.swing.JPanel;
import java.awt.*;
import javax.swing.*;
import javax.swing.JLabel;

/*
**
**@author Agilan a/l Khali Thasan
**
*/
public class BoardSettings extends JPanel
{
    // The setting beside game board for exiting,saving and keeping track of the turn
    private int x;
    JButton saveButton;
    JButton exitButton;
    JLabel turnLabel;
    SaveFunction Save = new SaveFunction();
    /**
     * Constructor for objects of class BoardSettings
     */
    public BoardSettings(Controller cntrl,BoardLogicModel BML,View view)
    {
        this.setBounds(600,50,200,300);
        this.setBackground(Color.lightGray);
        this.setLayout(new GridLayout(2,1));
        saveButton = new JButton("SAVE");
        saveButton.addActionListener(e ->
        {
            try
            {
                 Save.SaveGame(BML,cntrl.turn);
                 view.doneSave();
            }
            catch (java.io.IOException ioe)
            {
                ioe.printStackTrace();
            }
        });
        this.add(saveButton);
        
        exitButton = new JButton("EXIT");
        exitButton.addActionListener(e -> System.exit(0));
        this.add(exitButton);
        
        turnLabel = new JLabel("TURN 1");
        turnLabel.setHorizontalAlignment(SwingConstants.CENTER);
        turnLabel.setVerticalAlignment(SwingConstants.CENTER);
        turnLabel.setBackground(Color.lightGray);
        this.add(turnLabel);
    }
    public void updateTurn(int turn)
    {
        turnLabel.setText("TURN "+turn);
    }
    
}

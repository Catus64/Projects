import javax.swing.JPanel;
import java.awt.*;
import javax.swing.*;
/**
 * Write a description of class MainView here.
 *
 * @author Agilan a/l Khali Thasan
 * 
 */
public class MainView extends JPanel
{
    JLabel mainLabel;
    JButton playButton;
    JButton insButton;
    /**
     * This is a Component of View for the main menu aka initial start page
     */
    public MainView(Controller cntrl,BoardLogicModel BML,View v)
    {
        this.setBounds(75,100,800,500);
        this.setBackground(Color.lightGray);
        this.setLayout(null);
        
        Populate(cntrl,BML,v);
        
    }
    public void Populate(Controller cntrl,BoardLogicModel BML,View v)
    {
        mainLabel = new JLabel("Kwazam Chess");
        mainLabel.setFont(new Font("Arial", Font.BOLD, 32));
        mainLabel.setBounds(300,50,300,200);
        this.add(mainLabel);
        
        playButton = new JButton("Start Game");
        playButton.setBounds(50,300,200,100);
        playButton.addActionListener(e -> cntrl.startGame(BML,v));
        this.add(playButton);
        
        insButton = new JButton("How to Play");
        insButton.setBounds(300,300,200,100);
        insButton.addActionListener(e -> v.instruction());
        this.add(insButton);
        
        JButton loadButton = new JButton("Load Game");
        loadButton.setBounds(550,300,200,100);
        loadButton.addActionListener(e -> cntrl.loadGame(BML,v));
        this.add(loadButton);
    
    }
    public void clear()
    {
        this.removeAll();
    }
    public void rePopulate()
    {
        this.add(mainLabel);
        this.add(playButton);
        this.add(insButton);
    }

    
}

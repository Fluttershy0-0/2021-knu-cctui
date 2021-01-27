package keylistener;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
 
public class TestFrame extends JFrame {
     
    private JLabel label;
     
    public TestFrame() {
        super(".tie5Roanl");
        createGUI();
    }


    public void createGUI() {
    	
    	
    	
    	  try (PrintWriter writer = new PrintWriter(new File("test.csv"))) {
    	        StringBuilder sb = new StringBuilder();
    	        sb.append("subject");
    	        sb.append("sessionIndex");
    	        sb.append("rep");
    	        sb.append("H.period");
    	        
    	        sb.append("DD.period.t");
    	        sb.append("UD.period.t");
    	        sb.append("H.t");
    	        
    	        sb.append("DD.t.i");
    	        sb.append("UD.t.i");
    	       sb.append("H.i");
    	       
    	        sb.append("DD.i.e");
    	        sb.append("UD.i.e");
    	        sb.append("H.e");
    	        
    	        sb.append("DD.e.five");
    	        sb.append("UD.e.five");
    	        sb.append("H.five");
    	        
    	        sb.append("DD.five.Shift.r");
    	        sb.append("UD.five.Shift.r");
    	        sb.append("H.Shift.r");
    	        
    	        sb.append("DD.Shift.r.o");
    	        sb.append("UD.Shift.r.o");
    	        
    	        sb.append("DD.o.a");
    	        sb.append("UD.o.a");
    	        sb.append("H.a");
    	        
    	        sb.append("DD.a.n");
    	        sb.append("UD.a.n");
    	        sb.append("H.n,");
    	        
    	        sb.append("DD.n.l");
    	        sb.append("UD.n.l");
    	        sb.append("H.l,");
    	        
    	        sb.append("DD.l.Return");
    	        sb.append("UD.l.Return");
    	        sb.append("H.Return");
    	        
    	
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        int pinmanychar = 10;
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        panel.setFocusable(true);
 
        label = new JLabel();
        label.setFont(new Font("Arial", Font.PLAIN, 40));
        label.setHorizontalAlignment(JLabel.CENTER);

        StringBuilder bs = new StringBuilder();
        panel.addKeyListener(new KeyAdapter() {
        	
        	double H;
            double DD;
            double UD;
            double keyPressedMillis;
            double keyReleased;
            int flag=0;
            
            
            
            
            
            
            
            
            
            
            
            public void keyReleased(KeyEvent e) {
            	
            	
            	
            	
            	flag++;
                label.setText(e.getKeyText(e.getKeyCode()));
                keyReleased = System.currentTimeMillis();
                H = keyReleased-keyPressedMillis;
                DD=UD+H;
//                System.out.println(H+"час утримання");
//                System.out.println(DD+"інтервал натискання1-натискання2");
//           	    System.out.println(UD+"інтервал відпускання1-натискання2");
                
                if(flag > 1) {
                	bs.append(DD/100);
                	bs.append(UD/100);
                }
                bs.append(H/100);
               if(flag==pinmanychar) {
            	   flag=0;
            	   bs.append('\n');
            	   System.out.println(bs);
            	   writer.write(bs.toString());
               }
              
            }
            public void keyPressed(KeyEvent e) {
            	 label.setText(e.getKeyText(e.getKeyCode()));
            	 keyPressedMillis = System.currentTimeMillis() ;
            	 UD = System.currentTimeMillis()-keyReleased;

            	 
		    }
            
        });
         
        panel.add(label, BorderLayout.CENTER);
                 
        setPreferredSize(new Dimension(350, 350));
        getContentPane().add(panel);
        



      } catch (FileNotFoundException e) {
        System.out.println(e.getMessage());}
        

        
    }

    

    
    
    public static void main(String[] args){

        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                JFrame.setDefaultLookAndFeelDecorated(true);
                TestFrame frame = new TestFrame();
                frame.pack();
                frame.setLocationRelativeTo(null);
                frame.setVisible(true);
            }
        });

    }}
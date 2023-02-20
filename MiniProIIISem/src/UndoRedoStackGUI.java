import java.util.Stack;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class UndoRedoStackGUI extends JFrame implements ActionListener
{
	JTextArea ta;
	UndoRedoStackGUI()
	{
		super("\tUNDO REDO\t");
		JMenu edit =new JMenu("Edit");
		JMenuItem undo=new JMenuItem("Undo");
		edit.add(undo);
		JMenuItem redo=new JMenuItem("Redo");
		edit.add(redo);
		ta=new JTextArea();
		JScrollPane sp=new JScrollPane(ta);
		add(sp,BorderLayout.CENTER);
		JMenuBar mb=new JMenuBar();
		mb.add(edit);
		setJMenuBar(mb);
		undo.addActionListener(this);
		redo.addActionListener(this);
	}
	static Stack<Character> Undo = new Stack<Character>();
	static Stack<Character> Redo = new Stack<Character>();
	public void actionPerformed(ActionEvent ae)
	{
		if(ae.getActionCommand().equals("Undo"))
		{
			try
			{
				String con = ta.getText();
				for(int  i = 0  ;  i < con.length(); i++){
					char var =  con.charAt(i);
					Undo.push(var);
				}
				Redo.push(Undo.pop());
				String undo_con ="";
				for (int i = 0; i < Undo.size(); i++) {
					undo_con += Undo.get(i);
				}
				ta.selectAll();
				ta.replaceSelection("");
				ta.setText(undo_con);
				Undo.clear();
			}
			catch(Exception e){}
		}
		if(ae.getActionCommand().equals("Redo"))
		{
			try
			{
				String con = ta.getText();
				for (int  i = 0  ;  i < con.length(); i++){
					char var =  con.charAt(i);
					Undo.push(var);
				}
				char X = (char)Redo.peek();
				Redo.pop();
				Undo.push(X);
				String con_redo = "";
				for (int i = 0; i < Undo.size() ; i++) {
					con_redo += Undo.get(i);
				}
				ta.selectAll();
				ta.replaceSelection("");
				ta.setText(con_redo);
				Undo.clear();
			}
			catch(Exception e){}
		}
	}
}
class SwingMenuTool
{
	public static void main(String[] args)
	{
		UndoRedoStackGUI f=new UndoRedoStackGUI();
		f.setSize(800,800);
		f.setVisible(true);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
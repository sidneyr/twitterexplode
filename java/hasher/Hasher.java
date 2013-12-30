import java.io.*;
import org.eclipse.swt.*;
import org.eclipse.swt.layout.*;
import org.eclipse.swt.events.*;
import org.eclipse.swt.widgets.*;
import javax.xml.bind.DatatypeConverter;
import java.security.MessageDigest;

public class Hasher {
    public static void main (String [] args) {
	Display display = new Display ();
	Shell shell = new Shell(display);
        RowLayout layout = new RowLayout(SWT.HORIZONTAL);
        layout.wrap = true;
        layout.fill = false;
        layout.justify = true;
        shell.setLayout(layout);

        Label label = new Label(shell, SWT.CENTER);
        label.setText("Enter a string to be hashed: ");

        final Text text = new Text(shell, SWT.BORDER);
        text.setLayoutData(new RowData(100, SWT.DEFAULT));

        Button hash = new Button(shell, SWT.PUSH);
        hash.setText("Hash Text");
        hash.addSelectionListener(new SelectionAdapter() {
                @Override
                public void widgetSelected(SelectionEvent e) {
                    MessageDigest md = null;
                    try{
                        md = MessageDigest.getInstance("SHA-256");
                    } catch (java.security.NoSuchAlgorithmException ex) {
                        throw new Error("Algorithm not found");
                    }
                    byte[] user_text = md.digest(text.getText().getBytes());
                    String user_text_str = DatatypeConverter.printHexBinary(user_text);
                    System.out.println(user_text_str);
                }
            });

        Button cancel = new Button(shell, SWT.PUSH);
        cancel.setText("Exit");
        cancel.addSelectionListener(new SelectionAdapter() {
                @Override
                public void widgetSelected(SelectionEvent e) {
                    System.exit(0);
                }
            });

        shell.setDefaultButton(hash);
        shell.pack();
        shell.open ();
        while (!shell.isDisposed ()) {
            if (!display.readAndDispatch ()) display.sleep ();
        }
        display.dispose ();
    }
}
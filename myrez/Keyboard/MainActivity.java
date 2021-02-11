package com.example.demodatacollector;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.os.Bundle;
import android.widget.TextView;


public class MainActivity extends Activity {

    TextView tvOut;
    Button btnOk;
    Button btnCancel;

    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // найдем View-элементы
        tvOut = (TextView) findViewById(R.id.textView);
        Button bt1 = (Button) findViewById(R.id.button29);
        Button bt2 = (Button) findViewById(R.id.button21);
        Button bt3 = (Button) findViewById(R.id.button20);
        Button bt4 = (Button) findViewById(R.id.button22);
        Button bt5 = (Button) findViewById(R.id.button1);
        Button bt6 = (Button) findViewById(R.id.button23);
        Button bt7 = (Button) findViewById(R.id.button24);
        Button bt8 = (Button) findViewById(R.id.button25);
        Button bt9 = (Button) findViewById(R.id.button26);
        Button bt0 = (Button) findViewById(R.id.button27);
        Button btEnter = (Button) findViewById(R.id.button30);


        tvOut.setText("");
        String[] arr;


        View.OnClickListener oclBt1 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                    tvOut.setText("1");
                }
        };
        View.OnClickListener oclBt2 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("2");
            }
        };
        View.OnClickListener oclBt3 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("3");
            }
        };
        View.OnClickListener oclBt4 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("4");
            }
        };
        View.OnClickListener oclBt5 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("5");
            }
        };
        View.OnClickListener oclBt6 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("6");
            }
        };
        View.OnClickListener oclBt7 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("7");
            }
        };
        View.OnClickListener oclBt8 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("8");
            }
        };
        View.OnClickListener oclBt9 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("9");
            }
        };
        View.OnClickListener oclBt0 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("0");
            }
        };
        View.OnClickListener oclBtEnter = new View.OnClickListener() {
            @SuppressLint("SetTextI18n")
            @Override
            public void onClick(View v) {
                tvOut.setText("Finished");
            }
        };


        bt1.setOnClickListener(oclBt1);
        bt2.setOnClickListener(oclBt2);
        bt3.setOnClickListener(oclBt3);
        bt4.setOnClickListener(oclBt4);
        bt5.setOnClickListener(oclBt5);
        bt6.setOnClickListener(oclBt6);
        bt7.setOnClickListener(oclBt7);
        bt8.setOnClickListener(oclBt8);
        bt9.setOnClickListener(oclBt9);
        bt0.setOnClickListener(oclBt0);
        btEnter.setOnClickListener(oclBtEnter);

    }
}

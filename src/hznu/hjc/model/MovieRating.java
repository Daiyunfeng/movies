package hznu.hjc.model;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
public class MovieRating
{
	//private int id;
	
	private int userId;
	
	private int movieId;
	
	//评分
	private double rate;
	
	//时间戳
	private int timeStamp;
	
	public static Comparator<MovieRating> sortByRate = new Comparator<MovieRating>()
	{
		
		@Override
		public int compare(MovieRating o1, MovieRating o2)
		{
			return o1.getRate()>=o2.getRate()?1:-1;
		}
	};
}

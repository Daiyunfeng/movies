package hznu.hjc.util;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

import hznu.hjc.model.MovieRating;

public class DataFileUtil
{

	public static ArrayList<MovieRating> getRatingFromFile(String filePath)
	{
		ArrayList<MovieRating> movieRatings = new ArrayList<>();
		try
		{
			BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(filePath)));
			String data = null;
			while ((data = br.readLine()) != null)
			{
				String[] strs = data.split("	");
				MovieRating temp = new MovieRating();
				temp.setUserId(Integer.parseInt(strs[0]));
				temp.setMovieId(Integer.parseInt(strs[1]));
				temp.setRate(Double.parseDouble(strs[2]));
				temp.setTimeStamp(Integer.parseInt(strs[3]));
				movieRatings.add(temp);
			}
			br.close();
		}
		catch (IOException e)
		{
			// TODO: handle exception
			e.printStackTrace();
		}
		return movieRatings;
	}
}

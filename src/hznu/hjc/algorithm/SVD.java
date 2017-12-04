package hznu.hjc.algorithm;

import java.io.File;
import java.util.ArrayList;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

import hznu.hjc.model.MovieRating;
import hznu.hjc.util.DataFileUtil;
import lombok.Getter;
import lombok.Setter;

public class SVD
{
	private static SVD instance = null;
	private ReentrantReadWriteLock lock;
	private Lock readLock;
	private Lock writeLock;
	private final String folder = "//result//";
	
	private ArrayList<MovieRating> movieRatings;
	
	// 训练步数
	private int steps;
	
	// 分解的矩阵为uk
	private int k;
	
	// 梯度下降参数
	private double gamma;
	
	// 防止过拟合
	private double lambda;

	private double[] bi;	//27278*1
	private double[] bu;	//131262*1
	private double[][] qi;	//27278*30
	private double[][] pu;	//131262*30
	//电影对应用户的评分
	private ArrayList<double[]> movieToUser;
	//用户对应电影的评分
	private ArrayList<double[]> user_movie;

	public static SVD getInstance()
	{
		if (instance == null)
		{
			instance = new SVD();
		}
		return instance;
	}

	private SVD()
	{
		lock = new ReentrantReadWriteLock();
		readLock = lock.readLock();
		writeLock = lock.writeLock();
		steps = 30;
		k = 30;
		gamma = 0.04;
		lambda = 0.11;
		movieRatings = DataFileUtil.getRatingFromFile("G:\\推荐系统数据\\ml-100k\\ml-100k\\u1.base");
		init();
	}
	
	private void init()
	{
		File biFile = new File(folder + "bi.txt");
		File buFile = new File(folder + "bu.txt");
		File qiFile = new File(folder + "qi.txt");
		File puFile = new File(folder + "pu.txt");
		if(biFile.exists() && buFile.exists() && qiFile.exists() && puFile.exists())
		{
			
		}
	}
	
	/**
	 * 当movieRatings变化的特别大的时候 更新一下bi bu qi pu
	 * 并且把这4个矩阵存储起来 先分别存储到一个临时文件 再同时修改文件
	 * 防止写到目标文件中途服务器被关闭
	 */
	public static void update()
	{
		
	}
	
	private void train()
	{

	}
}

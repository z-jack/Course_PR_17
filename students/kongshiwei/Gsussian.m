[b] = xlsread('mix.xlsx',1,'A1��D1628');
%��һ��
x = b(:,1)/max(b(:,1));
y = b(:,2)/max(b(:,2));
c = zeros(1682,1);
axis=[x,y];
%�Ѿ������ݼ��������������ֱ��ȡǰ23����Ϊ����
data = [x(1:32,1),y(1:32,1)];
p = (zeros(23,1)+1)/23;
variance = cell(1,23);
for i = 1:23
    variance{i} = [0.1 0;0 0.1];
end
r = zeros(1628,23);
for q =1:40
for i = 1:1628
    sumR = 0;
    for j = 1:23
        sumR = sumR+1/sqrt(det(variance{j}))*exp(-0.5*(axis(i,:)-data(j,:))/variance{j}*((axis(i,:)-data(j,:)).'))*p(j,1);
    end
    for k = 1:23
        r(i,k) = 1/sqrt(det(variance{k}))*exp(-0.5*(axis(i,:)-data(k,:))/variance{k}*((axis(i,:)-data(k,:)).'))*p(j,1)/sumR;
    end
end
for m = 1:23
    tempD = [0,0];
    %���¾�ֵ
    for n =1:1628
       tempD = tempD + r(n,m)*axis(n,:); 
    end
    data(m,:) = tempD/sum(r(:,m));
    %���·���
    tempV = zeros(2,2);
    for n = 1:1628
        tempV = tempV + r(n,m)*((axis(n,:)-data(m,:)).'*(axis(n,:)-data(m,:)));
    end
    variance{m} = tempV/sum(r(:,m));
    %����ϵ��
    p(m) = sum(r(:,m))/1628;
end
end
for i = 1:1628
    [mi,index] = max(r(i,:));
    c(i)=index;
end
%��ͼ
for i = 1:1628
    rand('seed',c(i,1));
    color = rand(1,3);
    plot(x(i,1),y(i,1),'*','color',color);
    hold on;
end   
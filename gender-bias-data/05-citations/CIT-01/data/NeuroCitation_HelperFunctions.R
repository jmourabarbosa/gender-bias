##################################################################################
####### This code and data has been compiled by Jordan Dworkin to accompany ######
## "The extent and drivers of gender imbalance in neuroscience reference lists" ##
############## (https://www.nature.com/articles/s41593-020-0658-y) ###############
######### Please email jordandworkin@gmail.com with questions or requests ########
##################################################################################

transform.cat.4=function(x){
  ifelse(x%in%c("MM","WM","MW","WW"),x,"NA")
}
transform.cat.2=function(x){
  ifelse(x=="MM",x,
         ifelse(x%in%c("WM","MW","WW"),"W|W","NA"))
}
citeprops=function(ref_proportions,i=NULL,type='conditional'){
  if(is.null(i)){i=1:nrow(ref_proportions)}
  if(type=='conditional'){
    nas=apply(is.na(ref_proportions[i,c(1:12)]),1,sum)!=0
    i=i[!nas]
    out=round(matrix(apply(ref_tot_sub[i,c(1:4,9:12)],2,sum)/
                       sum(apply(ref_tot_sub[i,1:4],2,sum)),
                     byrow=T,ncol=4),3)
    rownames(out)=c("Observed props.","Expected props.")
  }else if(type=='randomdraw'){
    nas=apply(is.na(ref_proportions[i,c(1:12)]),1,sum)!=0
    i=i[!nas]
    out=round(matrix(apply(ref_tot_sub[i,c(1:4,5:8)],2,sum)/
                       sum(apply(ref_tot_sub[i,1:4],2,sum)),
                     byrow=T,ncol=4),3)
    rownames(out)=c("Observed props.","Expected props.")
  }else{
    stop("'type' must be either 'conditional' or 'randomdraw'")
  }
  colnames(out)=c("MM","WM","MW","WW")
  return(out)
}
citegap=function(ref_proportions,i=NULL,type='conditional'){
  if(is.null(i)){i=1:nrow(ref_proportions)}
  if(type=='conditional'){
    nas=apply(is.na(ref_proportions[i,c(1:12)]),1,sum)!=0
    i=i[!nas]
    out=apply(ref_proportions[i,1:4],2,sum)/
      apply(ref_proportions[i,9:12],2,sum)-1
  }else if(type=='randomdraw'){
    nas=apply(is.na(ref_proportions[i,c(1:12)]),1,sum)!=0
    i=i[!nas]
    out=apply(ref_proportions[i,1:4],2,sum)/
      apply(ref_proportions[i,5:8],2,sum)-1
  }else{
    stop("'type' must be either 'conditional' or 'randomdraw'")
  }
  names(out)=c("MM","WM","MW","WW")
  return(out)
}
netgap=function(network_measure,i=NULL,groups,cites,verbose=F){
  if(is.null(i)){i=1:length(network_measure)}
  network_measure=network_measure[i]
  groups=groups[i]
  cites=cites[i]
  vals=suppressWarnings(summary(rq(network_measure~groups,
                                   weights=cites)))
  vals=as.numeric(vals$coefficients[1:4,1])
  vals=c(vals[1],vals[2:4]+vals[1])
  if(verbose==T){
    names(vals)=c("Among MM","Among WM","Among MW","Among WW")
    return(vals)
  }else{
    return(vals)
  }
  
}
medover=function(mm_overcite,i=NULL,groups,cites,verbose=F,
                 network=F,ma_overrep=NULL,mmp_overrep=NULL){
  if(is.null(i)){i=1:length(mm_overcite)}
  mm_overcite=mm_overcite[i]
  groups=groups[i]
  cites=cites[i]
  if(network==F){
    vals=suppressWarnings(summary(rq(mm_overcite~groups,
                                     weights=cites)))
  }else if(network==T){
    if(!is.null(ma_overrep) & !is.null(mmp_overrep)){
      ma_overrep=ma_overrep[i]
      mmp_overrep=mmp_overrep[i]
      vals=suppressWarnings(summary(rq(mm_overcite~groups+
                                         ma_overrep+mmp_overrep,
                                       weights=cites)))
    }else{
      stop("Must include ma_overrep and mmp_overrep")
    }
  }
  vals=as.numeric(vals$coefficients[1:4,1])
  vals=c(vals[1],vals[2:4]+vals[1])
  if(verbose==T){
    names(vals)=c("Among MM","Among WM","Among MW","Among WW")
    return(vals)
  }else{
    return(vals)
  }
}
citegap.temp=function(citation.totals,i=NULL,years,return='mm'){
  if(is.null(i)){i=1:nrow(citation.totals)}
  nas=apply(is.na(citation.totals[i,c(1:12)]),1,sum)!=0
  i=i[!nas]
  unique.years=sort(unique(years),decreasing=F)
  years=years[i]
  citation.totals=citation.totals[i,]
  if(return=='all'){
    year.vals=matrix(0,nrow=length(unique.years),ncol=4)
    for(j in 1:length(unique.years)){
      tyear=unique.years[j]
      if(sum(years==tyear)>1){
        year.vals[j,]=apply(citation.totals[years==tyear,1:4],2,sum)/
          apply(citation.totals[years==tyear,9:12],2,sum)-1
      }else{
        year.vals[j,]=NA
      }
    }
    out=year.vals
  }else if(return=='mm'){
    year.vals=rep(0,length(unique.years))
    for(j in 1:length(unique.years)){
      tyear=unique.years[j]
      if(sum(years==tyear)>1){
        year.vals[j]=(sum(citation.totals[years==tyear,1])-
                        sum(citation.totals[years==tyear,9]))/
          sum(apply(citation.totals[years==tyear,9:12],2,sum))
      }else{
        year.vals[j]=NA
      }
    }
    out=summary(lm(year.vals~unique.years))$coefficients[2,1]
    out=round(out*100,6)
    names(out)=c("MM overcitation yearly trend (perc. points)")
  }else{
    stop("'return' must be either 'mm' or 'all'")
  }
  return(out)
}
citegap.temp2=function(citation.totals,i=NULL,years){
  if(is.null(i)){i=1:nrow(citation.totals)}
  nas=apply(is.na(citation.totals[i,c(1:12)]),1,sum)!=0
  i=i[!nas]
  unique.years=sort(unique(years),decreasing=F)
  years=years[i]
  citation.totals=citation.totals[i,]
  
  year.vals=matrix(0,nrow=length(unique.years),ncol=8)
  for(j in 1:length(unique.years)){
    tyear=unique.years[j]
    if(sum(years==tyear)>1){
      obs=apply(citation.totals[years==tyear,1:4],2,sum)
      exp=apply(citation.totals[years==tyear,9:12],2,sum)
      tot=sum(obs)
      year.vals[j,]=c(obs/tot,exp/tot)
    }else{
      year.vals[j,]=c(NA,NA)
    }
  }
  out=year.vals
  
  return(out)
}
netgap.temp=function(network_measure,i=NULL,groups,cites,years){
  if(is.null(i)){i=1:length(network_measure)}
  unique.years=sort(unique(years),decreasing=F)
  network_measure=network_measure[i]
  groups=groups[i]
  cites=cites[i]
  years=years[i]
  
  year.vals=matrix(0,nrow=length(unique.years),ncol=4)
  for(j in 1:length(unique.years)){
    tyear=unique.years[j]
    vals=c(median(rep(network_measure[years==tyear & groups=="MM"],
                      cites[years==tyear & groups=="MM"]),na.rm=T),
           median(rep(network_measure[years==tyear & groups=="WM"],
                      cites[years==tyear & groups=="WM"]),na.rm=T),
           median(rep(network_measure[years==tyear & groups=="MW"],
                      cites[years==tyear & groups=="MW"]),na.rm=T),
           median(rep(network_measure[years==tyear & groups=="WW"],
                      cites[years==tyear & groups=="WW"]),na.rm=T))
    year.vals[j,]=vals
  }
  out=year.vals
  
  return(out)
}
get.timedf=function(article.data,journal=NULL){
  if(is.null(journal)){
    timedata=NULL
    for(i in unique(article.data$PY)){
      subgends=article.data$AG[article.data$PY==i & 
                                 article.data$AG%in%c("MM","WM","MW","WW")]
      timedata.i=data.frame(Year=rep(i,4),Gender=c("MM","WM","MW","WW"),
                            Prop=c(mean(subgends=="MM"),
                                   mean(subgends=="WM"),
                                   mean(subgends=="MW"),
                                   mean(subgends=="WW")),
                            Color=c("darkslateblue","darkslategray4",
                                    "lightcyan3","lightsalmon3"))
      timedata=rbind(timedata,timedata.i)
    }
  }else{
    timedata=NULL
    if(!journal%in%article.data$SO){
      stop("'journal' must be one entered in the same format as article.data$SO")
    }
    for(i in unique(article.data$PY)){
      subgends=article.data$AG[article.data$PY==i & article.data$SO==journal &
                                 article.data$AG%in%c("MM","WM","MW","WW")]
      timedata.i=data.frame(Year=rep(i,4),Gender=c("MM","WM","MW","WW"),
                            Prop=c(mean(subgends=="MM"),
                                   mean(subgends=="WM"),
                                   mean(subgends=="MW"),
                                   mean(subgends=="WW")),
                            Color=c("darkslateblue","darkslategray4",
                                    "lightcyan3","lightsalmon3"))
      timedata=rbind(timedata,timedata.i)
    }
  }
  timedata$Color=as.character(timedata$Color)
  return(timedata)
}
get.plotdf=function(boot){
  plotdf=data.frame(Group=c("Man &\nMan","Woman &\nMan",
                            "Man &\nWoman","Woman &\nWoman"),
                    Prop=boot$t0,
                    LB=apply(boot$t,2,quantile,.025),
                    UB=apply(boot$t,2,quantile,.975))
  plotdf$Group<-factor(plotdf$Group,
                       levels=c("Man &\nMan","Woman &\nMan",
                                "Man &\nWoman","Woman &\nWoman"))
  return(plotdf)
}
get.plotdf.temp=function(boot,unique.years){
  plotdf=data.frame(Group=rep(c("Man &\nMan","Woman &\nMan","Man &\nWoman",
                                "Woman &\nWoman"),each=length(unique.years)),
                    Year=rep(unique.years,4),
                    Prop=as.vector(boot$t0),
                    LB=apply(boot$t,2,quantile,.025),
                    UB=apply(boot$t,2,quantile,.975))
  plotdf$Group<-factor(plotdf$Group,
                       levels=c("Man &\nMan","Woman &\nMan",
                                "Man &\nWoman","Woman &\nWoman"))
  return(plotdf)
}
get.plotdf.temp2=function(boot,unique.years){
  plotdf=data.frame(Year=rep(unique.years,8),
                    Type=c(rep("Observed",4*length(unique.years)),
                           rep("Expected",4*length(unique.years))),
                    Group=rep(rep(c("Man &\nMan","Woman &\nMan","Man &\nWoman",
                                    "Woman &\nWoman"),each=length(unique.years)),2),
                    Prop=as.vector(boot$t0),
                    LB=apply(boot$t,2,quantile,.025),
                    UB=apply(boot$t,2,quantile,.975))
  plotdf$Group<-factor(plotdf$Group,
                       levels=c("Man &\nMan","Woman &\nMan",
                                "Man &\nWoman","Woman &\nWoman"))
  plotdf=as.data.table(plotdf)
  
  return(plotdf)
}
get.ylim=function(plotdf1,plotdf2,group,type){
  if(type=="lower"){
    return(0.975*min(c(plotdf1$LB[plotdf1$Group==group],
                       plotdf2$LB[plotdf2$Group==group])))
  }else if(type=="upper"){
    return(1.025*max(c(plotdf1$UB[plotdf1$Group==group],
                       plotdf2$UB[plotdf2$Group==group])))
  }else{stop("'type' must be either 'lower' or 'upper'")}
}
equate.plotdf.lims=function(plotdf1,plotdf2){
  plotdf1[Group=="Man &\nMan",y_min:=get.ylim(plotdf1,plotdf2,
                                              "Man &\nMan","lower")]
  plotdf1[Group=="Man &\nMan",y_max:=get.ylim(plotdf1,plotdf2,
                                              "Man &\nMan","upper")]
  plotdf1[Group=="Woman &\nMan",y_min:=get.ylim(plotdf1,plotdf2,
                                                "Woman &\nMan","lower")]
  plotdf1[Group=="Woman &\nMan",y_max:=get.ylim(plotdf1,plotdf2,
                                                "Woman &\nMan","upper")]
  plotdf1[Group=="Man &\nWoman",y_min:=get.ylim(plotdf1,plotdf2,
                                                "Man &\nWoman","lower")]
  plotdf1[Group=="Man &\nWoman",y_max:=get.ylim(plotdf1,plotdf2,
                                                "Man &\nWoman","upper")]
  plotdf1[Group=="Woman &\nWoman",y_min:=get.ylim(plotdf1,plotdf2,
                                                  "Woman &\nWoman","lower")]
  plotdf1[Group=="Woman &\nWoman",y_max:=get.ylim(plotdf1,plotdf2,
                                                  "Woman &\nWoman","upper")]
  
  plotdf2[Group=="Man &\nMan",y_min:=get.ylim(plotdf1,plotdf2,
                                              "Man &\nMan","lower")]
  plotdf2[Group=="Man &\nMan",y_max:=get.ylim(plotdf1,plotdf2,
                                              "Man &\nMan","upper")]
  plotdf2[Group=="Woman &\nMan",y_min:=get.ylim(plotdf1,plotdf2,
                                                "Woman &\nMan","lower")]
  plotdf2[Group=="Woman &\nMan",y_max:=get.ylim(plotdf1,plotdf2,
                                                "Woman &\nMan","upper")]
  plotdf2[Group=="Man &\nWoman",y_min:=get.ylim(plotdf1,plotdf2,
                                                "Man &\nWoman","lower")]
  plotdf2[Group=="Man &\nWoman",y_max:=get.ylim(plotdf1,plotdf2,
                                                "Man &\nWoman","upper")]
  plotdf2[Group=="Woman &\nWoman",y_min:=get.ylim(plotdf1,plotdf2,
                                                  "Woman &\nWoman","lower")]
  plotdf2[Group=="Woman &\nWoman",y_max:=get.ylim(plotdf1,plotdf2,
                                                  "Woman &\nWoman","upper")]
  
  return(list(plotdf1,plotdf2))
}
f1plot=function(data,title,yl=T,xl=T){
  p=ggplot(data,aes(x=Year, y=Prop, fill=Color)) + 
    geom_area(alpha=0.9,size=.5,color="black")+theme_bw()+
    scale_fill_identity()+
    scale_x_continuous(limits=c(min(data$Year),max(data$Year)),
                       expand=c(0,0))+
    scale_y_continuous(limits=c(0,1),expand=c(0,0))+
    ggtitle(title)
  if(yl==T & xl==T){
    p+xlab("Year")+ylab("Proportion")
  }else{
    p
  }
}
f2plot=function(data,title,ymin,ymax,yl=T,xl=T,shortlab=F){
  p=ggplot(data,aes(x=Group, y=Prop, fill=Group))+
    geom_bar(stat="identity", color="black",position=position_dodge())+
    geom_errorbar(aes(ymin=LB,ymax=UB),width=.2)+
    theme_bw()+theme(legend.position="n")+
    geom_hline(yintercept=0,color='black',lty=1)+
    ggtitle(title)
  if(xl==T){
    p=p+xlab("Cited authors' gender (first & last)")
  }else{
    p=p+xlab(NULL)
  }
  if(shortlab==T){
    p=p+xlab("Cited authors")+
      scale_fill_manual(values=c("Overall"="gray24",
                                 "MM"="darkslateblue",
                                 "WM"="darkslategray4",
                                 "MW"="lightcyan3",
                                 "WW"="lightsalmon3"))
  }else{
    p=p+scale_fill_manual(values=c("Overall"="gray24",
                                   "Man &\nMan"="darkslateblue",
                                   "Woman &\nMan"="darkslategray4",
                                   "Man &\nWoman"="lightcyan3",
                                   "Woman &\nWoman"="lightsalmon3"))
  }
  if(yl==T){
    p=p+ylab("Percent over/undercitation")
  }else{
    p=p+ylab(NULL)
  }
  min.break=ceiling(ymin*10)/10
  max.break=floor(ymax*10)/10
  breaks=seq(min.break,max.break,(max.break-min.break)/4)
  p=p+scale_y_continuous(breaks=breaks,
                         limits=c(ymin,ymax))
  return(p)
}
f4Aplot=function(data,title,ymin,ymax){
  p=ggplot(data,aes(x=Year, y=Prop, color=Group))+
    geom_line()+
    geom_point()+
    geom_errorbar(aes(ymin=LB,ymax=UB),width=.2)+
    theme_bw()+theme(legend.position="n")+
    #ylab("Citation gap (obs % / exp %)")+
    ggtitle(title)+geom_hline(yintercept=0,color='black',lty=2)+
    scale_color_manual(values=c("Overall"="gray24",
                                "Man &\nMan"="darkslateblue",
                                "Woman &\nMan"="darkslategray4",
                                "Man &\nWoman"="lightcyan3",
                                "Woman &\nWoman"="lightsalmon3"))+
    ylab("Percent over/undercitation")+xlab("Year")
  
  min.break=ceiling(ymin*10)/10
  max.break=floor(ymax*10)/10
  breaks=seq(min.break,max.break,(max.break-min.break)/4)
  p=p+scale_y_continuous(breaks=breaks,
                         limits=c(ymin,ymax))
  
  return(p)
}
f4Bplot=function(data,title){
  p=ggplot(data,aes(x=Year, y=Prop, color=Group, lty=Type))+
    geom_line()+geom_point()+
    geom_errorbar(aes(ymin=LB,ymax=UB),width=.2)+
    facet_wrap(~Group, scales="free", nrow=2)+
    geom_blank(aes(y = data$y_min))+
    geom_blank(aes(y = data$y_max))+
    theme_bw()+ggtitle(title)+
    scale_color_manual(values=c("Overall"="gray24",
                                "Man &\nMan"="darkslateblue",
                                "Woman &\nMan"="darkslategray4",
                                "Man &\nWoman"="lightcyan3",
                                "Woman &\nWoman"="lightsalmon3"))+
    scale_linetype_manual(values=c("Observed"="solid","Expected"="dashed"))+
    ylab("Proportion of citations")+xlab("Year")+
    theme(legend.position="n",strip.background = element_blank(),
          strip.text.x = element_blank())
  return(p)
}
f5plot=function(data,title,ymin,ymax){
  min.break=ceiling(ymin*10)/10
  max.break=floor(ymax*10)/10
  breaks=seq(min.break,max.break,(max.break-min.break)/4)
  p=ggplot(data,aes(x=Year, y=Prop, color=Group))+
    geom_line()+
    geom_point()+
    geom_errorbar(aes(ymin=LB,ymax=UB),width=.2)+
    theme_bw()+theme(legend.position="bottom")+
    ggtitle(title)+geom_hline(yintercept=0,color='black',lty=2)+
    scale_color_manual(values=c("Man &\nMan"="#FDBC53",
                                "Woman &\nMan"="#798081",
                                "Man &\nWoman"="#95D5B2",
                                "Woman &\nWoman"="steelblue3"),
                       name="Citing\nauthors")+
    ylab("Median overrepresentation")+xlab("Year")+
    scale_y_continuous(breaks=breaks,limits=c(ymin,ymax))
  return(p)
}
f6plot=function(data,title,type,ymin,ymax){
  if(type=="A"){
    p=ggplot(data[data$Type=="A",])+
      geom_bar(aes(x=Group, y=Prop, fill=Group),
               stat="identity",color="black",position=position_dodge())+
      geom_errorbar(aes(x=Group,ymin=LB,ymax=UB),width=.2)
    
  }else{
    p=ggplot(data[data$Type=="B",])+
      geom_bar(aes(x=Group, y=Prop, fill=Group),
               stat="identity",color="black",position=position_dodge())+
      geom_errorbar(aes(x=Group,ymin=LB,ymax=UB),width=.2)+
      geom_bar(aes(x=data$Group[data$Type=="A"],y=data$Prop[data$Type=="A"]), 
               fill=NA,stat="identity",color="black",position=position_dodge(),
               lty="longdash")
  }
  min.break=ceiling(ymin*10)/10
  max.break=floor(ymax*10)/10
  breaks=seq(min.break,max.break,(max.break-min.break)/4)
  p+theme_bw()+theme(legend.position="n")+
    ggtitle(title)+xlab("Cited authors")+
    ylab("Percent over/undercitation")+
    scale_fill_manual(values=c("Man &\nMan"="#FDBC53",
                               "Woman &\nMan"="#798081",
                               "Man &\nWoman"="#95D5B2",
                               "Woman &\nWoman"="steelblue3"))+
    ylab("Median MM overcitation")+xlab(NULL)+
    scale_y_continuous(breaks=breaks,
                       limits=c(ymin,ymax))+
    geom_hline(yintercept=0,color='black',lty=1)
}